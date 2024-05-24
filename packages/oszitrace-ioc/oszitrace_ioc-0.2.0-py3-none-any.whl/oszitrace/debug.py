#!/usr/bin/python3

import numpy as np
import xarray as xr
import time, asyncio

import logging
logger = logging.getLogger(__name__)

import traceback

class AnimatedSinus:
    '''
    Debugging and simulation aid: animate a running sin() curve.
    '''
    
    def __init__(self, name,
                 display_proc=None,
                 dim=None,
                 coords=None,
                 start=0.0,
                 end=31.4,
                 numpts=512,
                 amplitude=1.0,
                 offset=0.0,
                 velocity=3.14,
                 frequency=1.0):
        '''
        Initializes a sin() animation.

        Args:

            name: the name of the dataset.
            display_proc: if not `None`, expected to be a callable which will
              be called on each frame of `.animate()` with the name as the
              first parameter, and the dataset (as `xarray.DataArray`) as the
              second.
            dim: if not `None`, expected to be the name of the X-axis. Defaults
              to `x`
            coord: if not `None`, expected to be the value set of the X-axis
              points. If it is None, this is put together from `start`, `end`
              and `numpts`. Otherwise all these values are extracted from `coord`.
              Optionally, `coord` can be a dictionary, xarray-style,
              with the key as the
              dimension name (see `dim`) and the value as the coordiantes.
            amplitude: Amplitude. Defaults to 1.0
            velocity: The angle by which the sin() function to shift, per second. Defaults
              to 3.14 (i.e. 180 degrees)
            start: the X-axis offset
            end: the last point of the X-axis
            numpts: number of points -- for the X-axis, and also for the sin()
              sampling data.
        '''
        self.name = name

        if coords is not None:
            if hasattr(coords, "keys"):
                dc = next(iter(coords.keys()))
                if dim is None:
                    self.dim = dc
                else:
                    if dc != dim:
                        raise RuntimeError(f'Dimension requested as "{dim}", but `coords\' specifies "{dc}"')
                    self.dim = dim
                self.coords = coords[self.dim]
            else:
                self.coords = coords
        else:
            np.linspace(start, end, numpts)

        self.ampl = amplitude
        self.offs = offset
        self.vel = velocity
        self.freq = frequency
        self.display_proc = display_proc

        # used for simulation
        self._t0 = time.time()
        self._tdelta = 0.0


    def set_display(self, display_proc):
        self.display_proc = display_proc


    @property
    def ydata(self):
        self._tdelta += (self.vel*(time.time()-self._t0))
        self._t0 = time.time()
        ydata = self.ampl * np.sin((self.coords+self._tdelta)*self.freq)
        return xr.DataArray(ydata, coords={self.dim: self.coords})


    async def animate(self, period=0.001):
        '''
        Convenience wrapper for an enless loop "animating" the sin()
        parameters, optionally calling a display update function
        for every new animation frame.
        The `display_proc` is expected to be a callable which receives
        a name as the first parameter and the data (as an `xarray.DataArray`)
        as the second.
        '''
        self.do_run = True
        try:
            while self.do_run:
                if display_proc is not None and hasattr(d, '__call__'):
                    display_proc(self.name, self.ydata)
                await asyncio.sleep(period)

        except Exception as e:
            logger.error(f"Sinus exception: {e}")
            logger.error(f"{traceback.format_exc()}")
            do_run = False
            logger.info(f'Sinus animation died a violent death')

        logger.info(f'Sinus animation died a peaceful death')
