#!/usr/bin/python3

import asyncio, logging, time, random, os

from oszitrace.debug import AnimatedSinus
from parse import parse

import numpy as np

from oszitrace.dialogue import *


class SimSinusDialogue:
    ''' Simulated oscilloscope wrapper, delivers a number if Sinus functions '''
    
    def __init__(self, env=None, log=None, coords=None, fail=0.0, triggered='auto',
                 **channels):
        '''
        Initializes the simulator with a number of channels.

        Args:
            env: List of env-vars to use.
            coords: Axis coordinates
            xvalues: Values of the X axis
            xname: Name of the X axis
            fail: Likelyhood that a particular channel retrieve "read"
              will fail, return a zero-length channel, etc. This is to
              simulate a bad read for error handling.
            channels: channel names and parameters. The channel names
             ("ch0", "ch1", ...) map to dictionaries containing the values
             `"offset"`, `"amplitude"`, `"frequency"` (in X axis units) and
             `"phase"` (in radians).
        '''
        if coords is None:
            coords = { 't': np.linspace(0.0, 6.28, 1000000) }

        self._log = log or logging.getLogger(__name__)
        self._env = env or os.environ

        if len(channels) == 0:
            channels = self._get_channels(env)

        self._sinmap = {
            k:AnimatedSinus(name=k, coords=coords, **(v or {})) \
            for k,v in channels.items()
        }

        self._params = {}

        self._trigger_mode = triggered if triggered in [ True, False] \
            else self._env.get('OSZI_SIM_TRIGGERED', 'no') in [ 'yes', '1', 'true' ]
        self._triggered = { k:False for k in self.channels }

        self._fail_probability = fail


    def _get_channels(self, env=None):
        d = env.get('OSZI_SIM_CHANNELS', 'default')
        return { k:None for k in d.split(':') }


    @property
    def channels(self):
        ''' Returns a list of channel names '''
        return tuple([k for k in self._sinmap.keys()])


    @property
    def parameters(self):
        return self._params


    async def init(self, init_chat=None):
        '''
        Asynchronous sync routine.

        If `init_chat` is not None, is exptected to be a list of {"q": ..., ["r": ...]}
        entries, which should be passed to the device on first connect / initialization.
        The "r" part is optional. If it is available, then a reply is expected from
        the device, which must match the (format) pattern. If it is not present,
        then the device must _not_ answer.
        If the format pattern is parsed using keys, the data extracted is stored,
        and made accessible, in the dictionary `.parameters`.

        The simulated version just "echoes" back the query string.
        '''
        self._log.info('Simulated async init')
        if init_chat is None:
            init_chat = []
        for xcg in init_chat:
            if 'r' in xcg:
                new_keys = parse(xcg['r'], xcg['q'])
                if new_keys is None:
                    raise DialogueParseError(f'Mesage: "{xcg['q']}", expected '
                                             f'format: "{xcg['r']}"')
                self._params.update(new_keys.named)
            await asyncio.sleep(0.1)


    async def retr_channel(self, ch=None, timeout=360.0):
        ''' Retrieves data for channel `ch`. '''
        t0 = time.time()
        while (self._trigger_mode == True) and (not self._triggered[ch]):
            if (time.time()-t0) > timeout:
                raise DialogueTimeoutRetry()
            await asyncio.sleep(0.01)
        self._triggered[ch] = False

        # Simulate empty dataset
        if random.random() < self._fail_probability:
            raise DialogueEmptyRetry()
        
        return self._sinmap[ch].ydata


    async def arm_trigger(self):
        '''
        Arms the trigger (if the oscilloscope is in any kind of
        triggered mode that needs arming). The trigger is not expected
        to be channel-specific.

        In simulation mode (controlled by init parameter or by
        env var), we only deliver data for each channel _once_
        after it's been triggered.
        '''
        for k in self._triggered.keys():
            self._triggered[k] = True

# Convenience name
Dialogue = SimSinusDialogue
