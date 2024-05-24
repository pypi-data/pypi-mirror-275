#!/usr/bin/python3

from os import environ
from emmi.scpi import MagicScpi

import numpy as np
import xarray as xr

import asyncio

from oszitrace.debug import AnimatedSinus
from oszitrace.agilent import AgilentDeviceConfig, AgilentDialogue
from oszitrace.lecroy import LecroyDeviceConfig, LecroyDialogue

import logging
logger = logging.getLogger(__name__)

import time

device_details = {
    'agilent': {
        'device_config': AgilentDeviceConfig,
        'dialogue': AgilentDialogue
    },
    
    'lecroy': {
        'device_config': LecroyDeviceConfig,
        'dialogue': LecroyDialogue
    }
}    

class ScpiTraces:

    def __init__(self, dev=None, rman="@py"):
        
        if dev is None:
            dev = environ.get("OSZI_DEVICE", "TCPIP::172.16.58.167::5025::SOCKET")

        self.dev_family = environ.get('OSZI_DEVICE_FAMILY', 'agilent')
        self.dev_config = device_details[self.dev_family]['device_config']
        logger.info(f'Device family \"{self.dev_family}\": {self.dev_config}')
            
        self.dev = MagicScpi(device=dev, device_conf=self.dev_config)

        self.dev_dialogue = device_details[self.dev_family]['dialogue'](self.dev)
        
        #self.tr = [
        #    AnimatedSinus("ch1", start=0.0, end=31.4, ampl=1.0, vel=3.14),
        #    AnimatedSinus("ch2", start=-10, end=10,   ampl=0.6, vel=6.28)
        #]


    async def init(self):
        return await self.dev_dialogue.init()


    #def get_traces_info(self):
    #    '''
    #    Returns a-priori plotting info for traces that are to be expected.
    #    '''
    #    return { t.name:t for t in self.tr }


    async def retr(self):
        '''
        Returns a list of trace data.
        '''
        data = {}
        for d in range(4):
            cdata = await self.dev_dialogue.retr_channel(d+1)
            if cdata is not None:
                data[cdata.name] = cdata
                
        return data
    
