#!/usr/bin/python3

import logging, asyncio

logger = logging.getLogger(__name__)

from caproto.server import PVGroup, pvproperty
from caproto import ChannelType

from oszitrace.dialogue import *

import traceback

class OsziChannelIOC(PVGroup):
    xoffset = pvproperty(dtype=ChannelType.FLOAT, doc="start of the axis")
    xdelta  = pvproperty(dtype=ChannelType.FLOAT, doc="stepping of the axis")
    xreach  = pvproperty(dtype=ChannelType.FLOAT, doc="the end point of the axis")

    def __init__(self, prefix, name, data_shape):

        super().__init__(prefix)

        if len(data_shape) != 1:
            raise RuntimeError(f'Not supporting multi-arrays yet')

        self._data_shape = data_shape

        # This is a hack to add .signal and .xaxis as PVs to the PVGroup.
        # This is essentially what (apparently) happens under the hood
        # in caproto's internals. There's likely a better way to do this,
        # I just can't figure this out from the docs or caproto code.
        self._signal  = pvproperty(dtype=ChannelType.FLOAT,
                                   max_length=data_shape[0],
                                   doc="the trace data",
                                   name=f'signal')
        self._xaxis   = pvproperty(dtype=ChannelType.FLOAT,
                                   max_length=data_shape[0],
                                   doc="the axis values",
                                   name=f'xaxis')
        for x in (self._signal, self._xaxis):
            tmp = x.pvspec.create(self)
            self.pvdb[tmp.pvname] = tmp
            if not hasattr(self, x.pvspec.name):
                setattr(self, x.pvspec.name, tmp)
            else:
                raise RuntimeError(f'Property "{x.pvspec.name}" already defined')

        self.name = name


    @property
    def full_pvdb(self):
        return self.pvdb

    async def update(self, new_data):
        try:
            # FIXME: for multi-arrays the shape would usually be
            # (N, 2) with N the number of points.
            # Need to decide how to return that (in two different PVs?
            # What about their axis?
            # Probably better handled in the Dialogue -- report an extra
            # channel for additonal arrays...(?))
            d = new_data.dims[0]
            size = new_data.shape[0]
            offs = new_data.coords[d].values[0]
            delt = (new_data.coords[d].values[-1]-offs) / size
            reac = offs + delt*size

            asyncio.gather(*(
                self.signal.write(new_data.values),
                self.xaxis.write(new_data.coords[d].values),
                self.xoffset.write(offs),
                self.xdelta.write(delt),
                self.xreach.write(reac),
            ), return_exceptions=False)
        except Exception as e:
            logger.error(f'Channel "{self.name}" update error: {e}')
    

class OsziTraceIoc(PVGroup):

    arm = pvproperty(dtype=ChannelType.LONG, doc="arm the trigger")
    
    def __init__(self, prefix, oszi, data_shape):
        '''
        Initializes the OsziTrace IOC.

        Args:
            prefix: the EPICS prefix to use
            oszi: the oszitrace Dialogue object to use.
              This must be instantiated and initialized
              (see the async `.init()` of Dialogue objects).
            length: The maximum length of all channels' signal PVs
              (FIXME: how to handle multi-array replies?
              should use `shape`? reshape data on incoming?)
              Typically this is extracted from the Dialogue
              channel data (`.retr_channel()`).
        '''
        self.oszi = oszi
        self.channels = {
            k:OsziChannelIOC(prefix=f'{prefix}{k}:',
                             name=k,
                             data_shape=data_shape) \
            for k in self.oszi.channels
        }

        super().__init__(prefix)


    @property
    def full_pvdb(self):
        p = {}
        p.update(self.pvdb)
        for k,v in self.channels.items():
            p.update(v.pvdb)
        return p

            
    @arm.putter
    async def arm(self, inst, val):
        pass


    async def update_channel(self, name):
        try:
            data = await self.oszi.retr_channel(name)
            await self.channels[name].update(data)
        except DialogueRetry:
            pass


    async def update(self):
        try:
            await asyncio.gather(*[
                self.update_channel(ch) for ch in self.channels
            ], return_exceptions=False)
        except Exception as e:
            logger.error(f'Device update error: {e}, '
                         f'traceback: {traceback.format_exc()}')
            raise
