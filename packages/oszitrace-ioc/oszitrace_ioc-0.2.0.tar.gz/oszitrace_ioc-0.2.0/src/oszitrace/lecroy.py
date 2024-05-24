#!/usr/bin/python3

import xarray as xr
import numpy as np

from concurrent.futures import ThreadPoolExecutor
from functools import partial

import logging, time, re, asyncio, traceback, struct, os
logger = logging.getLogger(__name__)

__all__ = [ "LecroyDialogue", "LecroyDeviceConfig" ]

LecroyDeviceConfig = { }

from oszitrace.dialogue import *
from oszitrace.dialogue import open_scpi_by_env

class TemplateNames:
    ''' Iterates through the template block names '''
    class Iterator:
        def __init__(self, lines, btype):
            self.itr = iter(lines)
            self.btype = btype
            
        def __next__(self):
            while True:
                line = next(self.itr).strip()
                if line.endswith(f': {self.btype}'):
                    return line[:line.rfind(f': {self.btype}')]
    
    def __init__(self, tr, btype):
        self.lines = tr.templ_text
        self.btype = btype

    def __iter__(self):
        return self.Iterator(self.lines, self.btype)


class TemplateBlock:

    class NotATypeItem(Exception): pass

    class TypeItem:

        item_pattern = re.compile('<[ ]*([0-9]*)>[ \t]*([_A-Z0-9]*):[ ]*([_a-z]*)')
        
        def __init__(self, text):
            
            m = self.item_pattern.findall(text)
            
            if len(m) == 0:
                logger.error(f'Cannot parse self-reported type item: "{text}"')
                raise TemplateBlock.NotATypeItem()
            
            n = m[0]
            
            self.position = int(n[0])
            self.field_name = n[1]
            self.field_type = n[2]
            self.struct_base_type = {
                'long': 'l',
                'word': 'h',
                'string': 's',
                'text': 's',
                'data': 's',
                'enum': 'h',
                'float': 'f',
                'double': 'd',
                'unit_definition': 's',
                'time_stamp': 's',
            }[self.field_type]
            self.struct_base_length = {
                'long': 4,
                'word': 2,
                'string': 1,
                'data': 1,
                'text': 1,
                'enum': 2,
                'float': 4,
                'double': 8,
                'unit_definition': 1,
                'time_stamp': 1,
            }[self.field_type]

            # only valid if this is an enum
            self.enum_type = {}
            self.enum_val = {}


        def add_enum_type(self, val, desc):
            self.enum_type[val] = desc
            self.enum_val[desc] = val


        def __str__(self):
            return f'TemplateBlock.TypeItem({self.field_type} @ {self.position}: {self.field_name})'

        def __repr__(self):
            return self.__str__()


    class Iterator:
        def __init__(self, tr, block_name, block_type):
            self.itr = iter(tr.templ_text)
            self.block_name = block_name
            self.block_type = block_type
            self._have_block = None


        def __next__(self):
            while True:
                line = self._clean_line(next(self.itr))
                
                if line is None:
                    continue

                ## Block starts with a "<name>: BLOCK"
                ## and ends with a "/00         ENDBLOCK"
                if line.startswith(f'{self.block_name}: ') \
                   and line.endswith(self.block_type):
                    self._have_block = True
                    continue
                
                if line.startswith('/00') \
                   and line.endswith(f'END{self.block_type}') \
                   and self._have_block == True:
                    self._have_block = False
                    raise StopIteration

                if self._have_block != True:
                    continue

                type_item = TemplateBlock.TypeItem(line)

                # the next lines up to "endenum" belong to this data type
                if type_item.field_type == 'enum':
                    while True:
                        t = self._clean_line(next(self.itr))
                        if t is None: continue
                        if t == 'endenum': break
                        (key, desc) = t.split()
                        assert key[0] == '_'
                        type_item.add_enum_type(int(key[1:]), desc)
                
                return type_item


        def _clean_line(self, line):
            # Returns a clean line -- no comments etc. Or `None` if the line is not usable.
            l2 = line
            comment = line.rfind(';')
            if comment != -1:
                l2 = l2[:comment]
            l2 = l2.strip()                    
            if len(l2) == 0:
                return None
            if l2[0] == ';':
                return None
            
            return l2
        
    
    def __init__(self, tr, block_name, block_type, bufsize=None):
        self.treader = tr
        self.block_name = block_name
        self.block_type = block_type

        self._fields = [i for i in self]
        self._bufsize = bufsize

        if self._bufsize is not None:
            self._format = self.get_format(bufsize=self._bufsize)
            self._struct = struct.Struct(self._format)


    def __iter__(self):
        return self.Iterator(self.treader, self.block_name, self.block_type)

    
    def guess_required_bufsize(self):
        # Returns what we think that our buffer requries.
        # Determining that is actually tricky... we only know the
        # size of the types, each of the (base) types, and offsets.
        # But for the last item, we can't tell if it's an array or
        # not. So we have to guess (assume).
        #
        # Running .get_format() will require a bufset

        if (self.block_type == "BLOCK"):
            if self._fields[-1].field_type not in ('string', 'data', 'text', 'time'):
                return self._fields[-1].position + self._fields[-1].struct_base_length
            else:
                raise RuntimeError(f'Can\'t deterine size of final field type "{self._fields[-1].field_type}"')
        
        elif self.block_type == "ARRAY":
            raise RuntimeError(f'Guessing block sizes on ARRAY-type blocks '
                               f'will get you to the principal\'s office')

        raise RuntimeError(f"Don\'t know how to handle block type '{self.block_type}'")


    def get_format(self, bufsize=None, assume_single_last_item=None):
        ''' Returns a format string usable with `struct.unpack()` for `btype`. '''

        if bufsize == self._bufsize:
            return self._format

        if (bufsize is None) and (assume_single_last_item in (None, True)):
            bufsize = self.guess_required_bufsize()

        struct_string = "="
        start_pos = np.array([t.position for t in self._fields])
        end_pos = np.roll(start_pos, -1)
        end_pos[-1] = bufsize
        len_list = end_pos-start_pos

        s = 0
        for t,l in zip(self._fields, len_list):
            num_elements = int(np.floor(l / t.struct_base_length))
            if num_elements > 1:
                struct_string += f'{num_elements}{t.struct_base_type}'
            else:
                struct_string += f'{t.struct_base_type}'
            s += num_elements * t.struct_base_length
            #print(f'fmt {s:3}: \t {num_elements:2}*{t.struct_base_length} (base: {t.struct_base_type}, field: {t.field_name})')

        return struct_string

    
    def unpack(self, buf):
        ''' Wrapper around `.format()` and `struct.unpack()`. '''

        if self._bufsize == len(buf):
            st = self._struct
        else:            
            fmt = self.get_format(bufsize=len(buf))
            st = struct.Struct(fmt)

        names = [f.field_name for f in self._fields]
        data = st.unpack(buf)

        if len(data) != len(self._fields):
            raise RuntimeError(f'Number of fields does not match format specification -- this is a bug')
        
        return { k:v for k,v in zip(names, data) }
    


class TemplateReader:
    
    def __init__(self, dev):
        # We don't parse the first few and last few lines -- they're just
        # describing the master TEMPLATE object, and it's a slightly different format. Meh.
        self._templ_data = dev.query('TMPL?')
        self.templ_text = [l for l in self._templ_data.split('\n')[4:-3]]
        
        for l in self.templ_text:
            logger.debug(f'Template text: {l}')

        #for k in self.keys():
        #    print(f'Showing off block: {k}')
        #    print(f'{self[k]}')


    def blocks(self):
        return TemplateNames(self, "BLOCK")


    def arrays(self):
        return TemplateNames(self, "ARRAY")


    def keys(self):
        return [k for k in self.blocks()] + [k for k in self.arrays()]


    def __getitem__(self, name):
        if name in self.blocks():
            return TemplateBlock(self, name, "BLOCK")
        if name in self.arrays():
            return TemplateBlock(self, name, "ARRAY")
        raise KeyError(f'Don\'t know what or where "{name}" is')



class RawQuery:

    head_regex = re.compile('^([A-Z]*)([0-9]*):([A-Z]*) ([A-Z_0-9]*)$')

    class PayloadIterator:
        def __init__(self, rq):
            self.rq = rq
            self.payload_index = 0
            self.part_itr = iter(self.rq.payload_parts)

        def __next__(self):
            if self.payload_index >= len(self.rq.payload)-1:
                raise StopIteration()
            
            part_type = next(self.part_itr)

            fmt = self.rq.template[part_type]
            try:
                req_size = fmt.guess_required_bufsize()
                raw = self.rq.payload[self.payload_index:self.payload_index+req_size]
                data = fmt.unpack(raw)
                self.payload_index += req_size
                return data
            except RuntimeError:
                logger.error(f'Cannot parse data at index {self.payload_index}')
                req_size = None
                data = None
                raise
            

    def __init__(self, dev, query, qtype=None, channel=None, digital=None, template=None):
        '''
        Args:
            buf: data buffer
            source: "C" for channel, or "DIGITAL"
        '''

        if channel is not None:
            source = f'C{channel}'
        else:
            source = f'DIGITAL{digital}'
            
        if qtype is None:
            qtype = "ALL"

        self.template = template or TemplateReader(dev)

        self.reply = self._exec_query(dev, f'{source}:{query}? {qtype}')
        header_consumed, self.header, tmp = self._parse_header(self.reply)

        # Lecroy answer differs on the query-type.        
        # self.payload is where all the data is, and what's inside depends on
        # the query types. Each payload has the format '#Nnnnnnnnnn<data>',
        # and the specific <data> format is one of the ones supported by TemplateReader.
        self.payload_parts = {
            "DESC": ( "WAVEDESC", ),
            "TEXT": ( "USERTEXT", ),
            "TIME": ( "TIME", ),
            "DAT1": ( "DAT1", ),
            "ALL": ( "WAVEDESC", "USERTEXT", "TRIGTIME", "DATA_ARRAY_1", "DATA_ARRAY_2" ),
        }[qtype]

        payload_header_consumed, self.payload = self._extract_payload(tmp)

        # The +1 is for the \n at the end of the message
        accounted = len(self.payload) + header_consumed + payload_header_consumed + 1
        if len(self.reply) != accounted:
            raise RuntimeError(f'Received {len(self.reply)} bytes, {accounted} accounted for')

        logger.debug(f'Header: {self.header}, payload: {self.payload[0:30]}...')

        
    def _exec_query(self, dev, query_cmd):
        logger.debug(f'> {query_cmd}')
        dev.write(query_cmd)
        r = dev.read_raw()
        logger.debug(f'< {r[0:30]}...{r[-10:]}')
        return r
        

    def _parse_header(self, buf):
        # Returns the data from the reply-header and the first position after that.
        
        i = buf.find(b',')
        if (i == -1):
            raise RuntimeError(f'Can\'t understand header in: {buf[0:40]}...')
        head = buf[:i]
        
        head_data = self.head_regex.findall(head.decode('ascii'))[0]
        
        if len(head_data) != 4:
            raise RuntimeError(f'Expected 4 head elemts, got {len(head_data)}')

        return (len(head)+1,
                { 'channel_type': head_data[0],
                  'channel_no': int(head_data[1]),
                  'reply_type': head_data[2],
                  'payload_type': head_data[3] },
                buf[i+1:])

    
    def _extract_payload(self, buf):
        # returns the payload type and data buffer
        if buf[0:1] != b'#':
            raise RuntimeError(f'Expecting size spec "#...", got '
                               f'{buf[0:1]} of {buf[0:10]} instead')

        s1 = int(buf[1:2].decode('ascii'), base=16)
        s2 = int(buf[2:2+s1].decode('ascii'))

        block_payload = buf[s1+2:s1+2+s2]
        payload_header_consumed = s1+2
        payload_data_consumed = s2

        return (payload_header_consumed, block_payload)


    def __iter__(self):
        return self.PayloadIterator(self)


    def first(self):
        return next(iter(self))

        
class WaveformQuery(RawQuery):
    def __init__(self, dev, *args, **kwargs):
        super().__init__(dev, *args, query="WF", **kwargs)


class LecroyDialogue:
    def __init__(self, env=None, log=None, magic_dev=None):
        
        if magic_dev is not None:
            self.dev = magic_dev
        else:
            self.dev = open_scpi_by_env(env=os.environ, log=log)

        self._chan = self._init_channels(env)

        # This class is supposed to be async, but VICP communication
        # is synchronous. We need to put everything related to that
        # in a separate thread.
        self._lock = asyncio.Lock()
        self._loop = asyncio.get_event_loop()
        self._exectr = ThreadPoolExecutor()

        
    def _init_channels(self, env):
        # initializes channel (names)
        cspec = env.get('OSZI_LECROY_CHANNELS',
                        env.get('OSZI_CHANNELS', 'ch1:ch2:ch3:ch4'))
        return cspec.split(':')


    def _channel_id(self, cname):
        # Returns the channel ID, starting with 1
        return self.channels.index(cname)+1


    async def init(self, init_talk=None):
        logger.info(f'Setting up waveform query for channels 1-4, streaming mode')

        self.dev_idn = self.dev.query("*IDN?")
        logger.info(f'Connected to: {self.dev_idn}')
        self._params = { 'id': self.dev_idn, }
        self._params.update(await self._init_talk(init_talk))

        self.format_template = TemplateReader(self.dev.kdev)
        logger.info(f'Retrieved payload formats: {[f for f in self.format_template.blocks()]}')
        logger.info(f'Retrieved array formats: {[f for f in self.format_template.arrays()]}')


    async def _init_talk(self, talk_obj):
        return {}


    async def _wait4sio(self, func, *args, **kw):
        '''
        Runs callable `func(*args, **kw)` in a separate thread
        and awaits for its completion.
        '''
        async with self._lock:
            return await self._loop.run_in_executor(self._exectr, partial(func, *args, **kw))


    @property
    def parameters(self):
        return self._params


    @property
    def channels(self):
        return self._chan
    
        
    async def _channel_info(self, ch=None):
        '''
        Returns name, expected number of points, and axis informations
        for the specified channel. The keys are for 
        '''

        try:
            desc_buf = await self._wait4sio(WaveformQuery, self.dev.kdev,
                                            channel=ch, qtype="DESC",
                                            template=self.format_template)
            
            desc = desc_buf.first()
            numpts = desc["WAVE_ARRAY_COUNT"]
            xoffset = desc["HORIZ_OFFSET"]
            xdelta = desc["HORIZ_INTERVAL"]
            xreach = xoffset+numpts*xdelta
            yoffs = desc["VERTICAL_OFFSET"]
            yscale = desc["VERTICAL_GAIN"]

            #from pprint import pprint
            #pprint(desc)

            return {
                'name': f'ch{ch}',
                'xunits': desc["HORUNIT"].decode('ascii'),
                'xaxis': 't',
                'xoffset': xoffset,
                'xdelta': xdelta,
                'xreach': xreach,
                'numpts': numpts,
                'yscale': yscale,
                'yoffs': yoffs
            }

        except Exception as e:
            logger.error(f'CH-{ch} read error: {e}. Traceback follows: {traceback.format_exc()}')
            await asyncio.sleep(3)


    async def _channel_raw_data(self, ch=None):
        dat_buf = await self._wait4sio(WaveformQuery, self.dev.kdev, channel=ch,
                                       qtype="DAT1", template=self.format_template)
        return np.frombuffer(dat_buf.payload, dtype='b')


    async def retr_channel(self, channel_name=None):
        '''
        Reads data for specified channel.
        Returns an `xarray.DataArray` with the name set to the channel name,
        and whatever axis information was taken out of the corresponding
        `.channel_info()` call.
        '''

        ch = self._channel_id(channel_name)

        try:
            info = await self._channel_info(ch)
            sdata = await self._channel_raw_data(ch)
            
            if info['numpts'] != len(sdata):
                logger.error(f'Assuming BYTE format, but point buffer '
                             f'size is {len(sdata)} instead of expected {info["numpts"]}')
                max_size = max(info['numpts'], len(sdata))
                sdata = np.full((max_size, ), np.nan)
                return xr.DataArray(sdata,
                                    name=info['name'],
                                    coords={
                                        info['xaxis']: np.linspace(0, 0.1, max_size) 
                                    })
            

            ndata = info['yoffs'] + sdata.astype(float)*info['yscale']
            data_len = len(ndata)
        
            return xr.DataArray(ndata,
                                name=info['name'],
                                coords={
                                    info['xaxis']: np.linspace(info['xoffset'],
                                                               data_len*info['xdelta'],
                                                               data_len)
                                })
        except RuntimeError as e:
            logger.error(f'Oops: {e}, traceback: {traceback.format_exc(0)}')
            return None


# Convenient name
Dialogue = LecroyDialogue
