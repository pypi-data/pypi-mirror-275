#!/usr/bin/python3

##
## Generic testing routines for a Dialogue
##

import pytest, asyncio

from oszitrace.sim import SimSinusDialogue
from .conftest import DialogueTestBase

import numpy as np

class TestSimFixtures(DialogueTestBase):
    
    @pytest.fixture(scope='class')
    def dialogue(self):
        return SimSinusDialogue(
            coords={'t': np.linspace(0.0, 10.0, 1000)},
            ch0=None,
            ch1=None,
            ch2=None,
            ch3=None
        )

    @pytest.fixture(scope='class')
    def init_talk(self):
        return [
            { 'q': '1 pin 1 shot',
              'r': '{pins:d} pin {shots:d} shot' },
            { 'q': '9 little indian boys',
              'r': '{num:d} little {ethn} boys' }
        ]
