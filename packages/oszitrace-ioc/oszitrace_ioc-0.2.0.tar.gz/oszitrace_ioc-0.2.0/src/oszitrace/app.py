#!/usr/bin/python3

import logging

import asyncio, time
import traceback, sys, os

from oszitrace.display.waveform import WaveformMplWidget
from oszitrace.trace import ScpiTraces
from oszitrace.debug import AnimatedSinus

logger = logging.getLogger("oszitrace")

from emmi.scpi import MagicScpi

from caproto.asyncio.client import Context
from caproto import CaprotoTimeoutError
from emmi.ca.reader import AsyncMonitorMany

class OsziApplication:

    def __init__(self, fingerprint_pvs=None, storage_format=None, group_format=None):
        self.do_run = True
        self.display = WaveformMplWidget()
        self.traces = ScpiTraces()

        self.fingerprint_pvs = fingerprint_pvs

        if self.fingerprint_pvs is not None:
            self.pv_monitor = AsyncMonitorMany(pvs=self.fingerprint_pvs, subscribe=True)
            self.pv_monitor.subscribe_incoming(self.new_data_fingerprint)            

        self.storage_fmt = storage_format or os.environ.get("OSZI_H5FILE_FORMAT", "/tmp/waveform.cdf")

        # you can use {channel} and {osc_scannum}
        self.storage_group_fmt = group_format or os.environ.get("OSZI_H5GROUP_FORMAT", "{osc_scannum:1.0f}.1/oszi/{channel}")
        
        self.storage_fingerprint = None
        self.old_storage_fingerprint = None

        self._coarsen_samples = int(os.environ.get('OSZI_DISPLAY_COARSEN', '1000'))
        self._loop_period = float(os.environ.get('OSZI_PERIOD', '0.01'))


    def new_data_fingerprint(self, data_dict):
        try:
            fingerprint = { k.split(':')[-1]:data_dict[k].data[0] \
                            for k in data_dict.keys() }

            if len(fingerprint) < len(self.fingerprint_pvs):
                logger.info(f'Fingerprint {fingerprint} is too short')
                return # not enough fileds

            fname = self.storage_fmt.format(**fingerprint)
            logger.debug(f"New storage is: {fname} (from {fingerprint})")

            self.storage_file_name = fname
            self.storage_fingerprint = fingerprint
            
        except Exception as e:
            logger.error(traceback.format_exc())
            


    async def run(self, period=None):

        if period is None:
            period = self._loop_period

        await self.traces.init()

        try:

            ctx = Context()

            if self.fingerprint_pvs is not None:
                await self.pv_monitor.connect(ctx)

            # Necessary when doing continous reading instead of monitoring
            #monitor_task = asyncio.create_task(
            #    self.pv_monitor.monitor_loop(period=0.1)
            #)                

            display_task = asyncio.create_task(
                self.display.update_loop(period=period)
            )

            while self.do_run:
                data = await self.traces.retr()

                for i in (1, 2, 3, 4):
                    ch_name = f'ch{i}'
                    
                    if data[ch_name] is None:
                        continue

                    if len(data[ch_name]) == 0:
                        continue

                    self.display_channel(ch_name, data[ch_name], cnt=i)

                try:
                    if self.storage_fingerprint != self.old_storage_fingerprint:
                        self.store_data(data, self.storage_file_name)
                        self.old_storage_fingerprint = self.storage_fingerprint
                except Exception as e:
                    logger.error(f'Cannot save current scan: {e}')

                await asyncio.sleep(period)

            self.display.run_update_loop = False
            await display_task

        except Exception as e:
            logger.error(traceback.format_exc())
            self.do_run = False


    def display_channel(self, ch_name, local_d, cnt=0):
        colors = ("yellow", "red", "black", "green",
                  "blue", "orange", "purple", "magenta")
        
        if len(local_d) == 0:
            return
                    
        small_d = local_d.coarsen(**{
            local_d.dims[0]: self._coarsen_samples,
            'boundary': 'trim'
        }).mean()

        if ch_name not in self.display.traces:
            logger.info(f'Channel {ch_name} has color {colors[cnt-1]}')
            self.display.add_trace(ch_name, data=small_d, color=colors[cnt-1], ylim=(-5, +5))
        else:
            self.display.update_trace(ch_name, small_d)


    def store_data(self, data, fname):
        for k,d in data.items():
            if d is None:
                continue
            if len(d) == 0:
                continue
            grp = self.storage_group_fmt.format(channel=k, **self.storage_fingerprint)
            logger.info(f'Writing to {fname} # {grp}: {k}')
            logger.debug(f'{fname}: storing {k} as {grp}')
            d.to_netcdf(path=fname, mode='a', format='NETCDF4',
                        group=grp, engine='h5netcdf',
                        encoding={i: {'compression': 'lzf'} \
                                  for i in [k] + [j for j in d.dims]})

def main():

    logger.setLevel(os.environ.get("OSZI_LOG_LEVEL", "INFO"))
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logger.info(f'Starting')

    logging.getLogger('pyvisa').setLevel(logging.INFO)
    logging.getLogger('matplotlib').setLevel(logging.INFO)
    logging.getLogger('caproto').setLevel(logging.INFO)
    logging.getLogger('pyvicp').setLevel(logging.INFO)
    logging.getLogger('caproto.bcast.beacon').setLevel(logging.WARNING)
    logging.getLogger('h5py').setLevel(logging.INFO)

    
    app = OsziApplication(storage_format=None,
                          group_format=None,
                          fingerprint_pvs=("KMC-3_XPP:osc_scannum",
                                           "KMC-3_XPP:osc_state"))
    
    asyncio.run(app.run())

if __name__ == "__main__":
        
    main()
