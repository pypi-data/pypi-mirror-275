#!/usr/bin/python3

import time, asyncio
from matplotlib import pyplot as plt

import numpy as np
import xarray as xr

class WaveformMplWidget:
    ''' Displays one or more waveforms (on the same X-axis) using matplotlib.
    '''
    
    def __init__(self):
        bgcolor = '#404050'
        fgcolor = 'w'

        self.fig = plt.figure(facecolor=bgcolor)
        self.grid = self.fig.add_gridspec(1, 1) # width_ratios=[...], height_ratios=[...]
        self.ax_traces = self.fig.add_subplot(self.grid[0,0], facecolor=bgcolor)

        self.ax_traces.set_xlim(-0.00025, 0.0005)
        self.ax_traces.set_ylim(-20, 20)
        
        self.fig.tight_layout()
        self.fig.show()

        self.traces = {}


    def add_trace(self, name, data=None, **plot_args):
        '''
        Adds a named trace to the display. If data is specified, it must be an xarray.DataArray.
        '''
        
        if data is None:
            data = xr.DataArray(np.array([0, 1]), coords={'y': [0, 1]})
            
        p = data.plot(ax=self.ax_traces, **plot_args)
        tr = { 'line': self.ax_traces.lines[-1] }
        self.traces[name] = tr

        self.fig.tight_layout()

        
    def update_trace(self, name, data):
        '''
        Updates data of named trace. `data` must be an xarray.DataArray
        '''
        
        try:
            tr = self.traces[name]
        except KeyError:
            tr = self.add_trace(name, data)

        coords = data.coords[data.dims[0]]
        tr['line'].set_data(coords.values, data.values)
        
        self.fig.canvas.draw_idle()

        
    def update(self):
        # finally: redraw canvas
        self.fig.canvas.flush_events()


    async def update_loop(self, period=0.01):
        self.run_update_loop = True
        while self.run_update_loop:
            t0 = time.time()

            self.update()
            d = time.time()-t0
            sleep_time = period-d
            
            if sleep_time < 0:
                sleep_time = 0.001

            await asyncio.sleep(sleep_time)
