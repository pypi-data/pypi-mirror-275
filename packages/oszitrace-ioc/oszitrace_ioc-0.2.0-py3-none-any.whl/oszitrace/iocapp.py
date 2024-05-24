#!/usr/bin/python3

import logging, asyncio, importlib
logger = logging.getLogger(__name__)

from caproto.asyncio.server import Context as ServerContext
from caproto.asyncio.server import start_server

from oszitrace.ioc import OsziTraceIoc

class OsziIocApplication:
    def __init__(self, args, env):
        self.oszi_dialogue = self._conf_dialogue(env=env)
        logger.info(f'Oszi known as "{self.name}"')

        self._env = env
                            
        self.ioc_prefix = env.get('OSZI_EPICS_PREFIX', 'KMC3:XPP:OSZI:')
        self.init_talk = self._init_init_talk(env.get('OSZI_INIT_TALK', ''))

        for l in self.init_talk:
            logger.info(f'Init: {l}')    


    def _conf_dialogue(self,
                       mod_data=None, mod_envvar=None,
                       name_data=None, name_envvar=None,
                       env=None):
        # Returns a (module, object, name) tuple for the
        # Dialogue to use, given an env-var specification
        
        if mod_data is None:
            if mod_envvar is None:
                mod_envvar = 'OSZI_DIALOGUE'
            mod_data = env.get(mod_envvar, 'oszitrace.sim:SimSinusDialogue')
        dia = mod_data.split(':')
        
        if len(dia) == 2:
            mod, obj = dia
        else:
            mod, = dia
            obj = 'Dialogue'

        if name_data is None:
            if name_envvar is None:
                name_envvar = 'OSZI_NAME'
            name_data = env.get(name_envvar, mod.split('.')[-1])

        return mod, obj, name_data
    

    def _init_oszi(self, mod, cls=None, env=None):
        # Import an Oszi Dialogue from module `mod'. As a courtesy,
        # if `mod' does not exist on its own, `oszitrace.<mod>' is
        # tried.
        # `cls' is by default `Dialogue', which is true for all
        # built-in Oszitrace dialogue modules.
        
        if cls is None:
            cls = 'Dialogue'

        logger.info(f'Using device dialogue: "{cls}" from "{mod}"')
        try:
            try:
                dia_module = importlib.import_module(mod)
            except ModuleNotFoundError:
                dia_module = importlib.import_module(f'oszitrace.{mod}')
            dia_class = getattr(dia_module, cls)
        except Exception as e:
            logger.error(f'Dialogue fail: {e}')
            raise
            
        return dia_class(env=(env or {}))


    def _init_init_talk(self, fpath=None):
        try:
            from yaml import load, dump
            from yaml import CLoader as Loader, CDumper as Dumper
        except ImportError:
            from yaml import Loader, Dumper

        if len(fpath) > 0:
            data = load(open(fpath, 'r').read(), Loader=Loader)
            if data['type'] != 'oszitrace-ioc/ascii-talk':
                raise RuntimeError(f'Not supported init-talk type: {data["type"]}')
            if data['version'] != '0.1':
                raise RuntimeError(f'Not supported init-talk version: {data["version"]}')
            return data['init']
        else:
            return []


    @property
    def name(self):
        return self.oszi_dialogue[2]
        

    async def run(self, period=0.1):
        self.do_run = True

        self.oszi = self._init_oszi(*(self.oszi_dialogue[:2]),
                                    env=self._env)
        await self.oszi.init()

        # Must retrieve a data sample to calculate the length...
        # FIXME: should fix this in the Dialogue API? Sometimes
        # this is available in the oscilloscope device not related
        # to capturing data, and conversely captured data isn't available
        # until a trigger has been armed and occured. But then
        # again, there's never a guarantee that each signal
        # is going to have the same length -- e.g. if the user
        # manipulates the hardware, the signal size(s) might change
        # on the fly. In that case we'd need to bail out anyway...

        if len(self.oszi.channels) > 0:
            ch_sample = await self.oszi.retr_channel(self.oszi.channels[0])
            ch_shape = ch_sample.shape
        else:
            ch_shape = None
        
        self.ioc = OsziTraceIoc(prefix=f'{self.ioc_prefix}{self.name}:',
                                oszi=self.oszi,
                                data_shape=ch_shape)
        
        
        for k in self.ioc.full_pvdb:
            logger.info(f'  {k}: {self.ioc.full_pvdb[k]}')

        self.ioc_task = asyncio.create_task(start_server(self.ioc.full_pvdb),
                                            name='oszi_ioc')
        while self.do_run:
            await asyncio.gather(*(
                self.ioc.update(),
                asyncio.sleep(period)
            ), return_exceptions=True)

        try:
            logger.info(f'Killing IOC')
            self.ioc_task.cancel()
            await self.ioc_task
        except Exception as e:
            logger.info(e)
