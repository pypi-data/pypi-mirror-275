#!/usr/bin/python3

from caproto.sync.client import read as ca_read, write as ca_write
from caproto import CASeverity

import pytest, asyncio, sys, os, random, string, time


class TestIocBasic:

    # ioc_args and ioc_env fixtures defined here will ultimately
    # end up as argumens to oszitrace.iocmain:run_ioc().
    # OSZI_EPICS_PREFIX is set by default, but can be overwritten
    # here (why whould you?)
    
    @pytest.fixture(scope='class')
    def ioc_args(self):
        return []

    @pytest.fixture(scope='class')
    def ioc_env(self):
        return {
            'OSZI_DIALOGUE': 'oszitrace.sim:SimSinusDialogue',
            'OSZI_NAME': 'test_oszi'
        }
    
    def test_ioc_vars(self, oszi_ioc):
        # VERY basic IOC test: essentially just makes sure the IOC
        # fires up, finds a device (by env-vars), and reacts to all PVs
        # that we know of.
        
        now = time.time()

        oz_dev = 'test_oszi' # see OSZI_NAME above
        oz_ch = 'default'    # first channel of SimSinusDialogue is "default"
        
        prefix = oszi_ioc['prefix']

        # single-instance variables (i.e. once per device, not per channel)
        ro_variables = [
            'xoffset',
            'xdelta',
            'xreach',
            'xaxis',
            'signal'
        ]


        for v in ro_variables:
            pv = f'{prefix}{oz_dev}:{oz_ch}:{v}'
            tm = f'{(time.time()-now):.5f}'
            print(f'{tm}: Querying: {pv}')
            s = ca_read(pv)

            if len(s.data) == 1:
                print(f'{tm}:   got {v}: {s.data[0]}')
            else:
                print(f'{tm}:   array {v}: {len(s.data)} items'
                      f' (min: {min(s.data)}, max: {max(s.data)})')

            assert s.status.severity == CASeverity.SUCCESS
