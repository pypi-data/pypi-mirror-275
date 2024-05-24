#!/usr/bin/python3

import asyncio, pytest, time, sys, os, random, string
import multiprocessing as mp
from oszitrace.iocmain import init_ioc, run_ioc

##
## To make it easier to test APIs, we define here all the tests
## (based on properties mostly, be sure to not include any device
## specific assersions here!) and just define specific fixtures
## in device-specific tests.
##

class DialogueTestBase:

    @pytest.mark.asyncio
    async def test_init(self, dialogue, init_talk):
        # First things first: device initialization.
        await dialogue.init(init_talk)


    @pytest.mark.asyncio
    async def test_retr_channel(self, dialogue):
        # Tests existence and rough behavior of .retr_channel
        assert len(dialogue.channels) > 0
        for c in dialogue.channels:
            dat = await dialogue.retr_channel(c)
            assert len(dat.shape) == 1

            
    def test_parameters(self, dialogue, init_talk):
        # Tests existence of the .parameters dictionary
        print(f'Params: {dialogue.parameters}')
        for msg in init_talk:
            if 'r' in msg:
                # everything we need to format 'r' should be
                # available in .parameters
                s = msg['r'].format(**(dialogue.parameters))


    @pytest.mark.asyncio
    async def test_arm_trigger(self, dialogue):
        await dialogue.arm_trigger()



@pytest.fixture(scope='session', autouse=True)
def session_prefix():
    p = ''.join(random.choice(string.ascii_lowercase) \
                for i in range(6))
    sp = os.environ.get('KRONOS_SESSION_PREFIX', p)
    print(f'Session IOC prefix: "{sp}"')
    return str(sp)
    

@pytest.fixture(scope='class')
def oszi_ioc(ioc_prefix, ioc_args, ioc_env):

    _ioc_env = {
        'OSZI_EPICS_PREFIX': ioc_prefix
    }
    _ioc_env.update(ioc_env)
    
    p = mp.Process(target=run_ioc,
                   kwargs={
                       'args': ioc_args,
                       'env': _ioc_env
                   })

    ## daemon mode will ensure that IOC exits when main process exits
    p.daemon = True
    p.start()
    
    return {'process': p,
            'prefix': ioc_prefix}


@pytest.fixture(scope='session')
def ioc_prefix(session_prefix):
    return f'{session_prefix}:'
