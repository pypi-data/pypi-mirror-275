#!/usr/bin/python3

import xarray as xr
import numpy as np

import logging
logger = logging.getLogger(__name__)

__all__ = [ "AgilentDialogue", "AgilentDeviceConfig" ]

AgilentDeviceConfig = {
    "read_termination": "\n",
    "write_termination": "\n"
}

class AgilentDialogue:
    def __init__(self, magic_dev):
        self.dev = magic_dev


    async def init(self):

        for s in range(3):
            logger.info(f'Querying device identification for {dev} in {3-s}...')
            time.sleep(1)

        self.dev_idn = self.dev.query("*IDN?")
        logger.info(f'Connected to: {self.dev_idn}')            
        
        logger.info(f'Setting up waveform query for channels 1-4, streaming mode')
        self.dev.write(':WAV:FORM ASC')
        self.dev.write(f':WAV:STR ON')
    
        
    async def _channel_info(self, ch=None):
        '''
        Returns name, expected number of points, and axis information
        for the specified channel. The keys are for 
        '''

        self.dev.write(f':WAV:SOUR CHAN{ch}')
            
        xdelt = await self.dev.async_query(':WAV:XINC?', parser=float)
        xoffs = await self.dev.async_query(':WAV:XOR?',  parser=float)
        xrang = await self.dev.async_query(':WAV:XRAN?', parser=float)
        
        units = await self.dev.async_query(':WAV:XUN?')
        axname = {
            'UNKNown': 'x',
            'SECond': 't',
            'VOLT': 'V',
            'CONStant': 'x',
            'AMP': 'x',
            'DECubels': 'I',
            'HERTz': 'f',
            'WATT': 'P'
        }[units]

        numpt = await self.dev.async_query(':WAV:POIN?', parser=int)
        cmpl  = await self.dev.async_query(':WAV:COMP?', parser=int)

        return {
            'name': f'ch{ch}',
            'units': units,
            'xaxis': axname,
            'xoffset': xoffs,
            'xdelta': xdelt,
            'xreach': xrang,
            'numpts': numpt
        }


    async def retr_channel(self, ch=None):
        '''
        Reads data for specified channel.
        Returns an `xarray.DataArray` with the name set to the channel name,
        and whatever axis information was taken out of the corresponding
        `.channel_info()` call.
        '''
        
        info = await self._channel_info(ch)
        sdata = await self.dev.async_query(":WAV:DATA?")
        ndata = np.array(sdata.split(','))[:-1].astype(float)
        
        #print(f'Num points: {len(ndata)}, {(xrang-xoffs)/xdelt}, {numpt}, '
        #      f'Units: {units}, from {xoffs} to {xrang}, delta {xdelt}, complete: {cmpl}%')

        data_len = len(ndata)
        
        return xr.DataArray(ndata,
                            name=info['name'],
                            coords={
                                info['xaxis']: np.linspace(info['xoffset'],
                                                           data_len*info['xdelta'],
                                                           data_len)
        })
