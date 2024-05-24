#!/usr/bin/python3

from os import environ
from emmi.scpi import MagicScpi

import logging
logger = logging.getLogger(__name__)

class DialogueError(Exception): pass

class DialogueRetry(Exception): pass

class DialogueParseError(DialogueError): pass

# Typically raised on communication errors (or not used at all,
# because we generically let the underlying errors pop up).
class DialogueTimeoutError(DialogueError): pass

# Typically raised when waiting for signals (e.g. triggers)
# that never come.
class DialogueTimeoutRetry(DialogueRetry): pass

class DialogueEmptyRetry(DialogueRetry): pass

__all__ = [ "DialogueParseError",
            "DialogueTimeoutError",
            "DialogueTimeoutRetry",
            "DialogueEmptyRetry",
            "DialogueError",
            "DialogueRetry" ]

def open_scpi_by_env(env=None, default_args=None, log=None):
    '''
    Returns an MagicScpi device, based on a number of environment variables.
    
    This is used in conjunction with configurable device backends, which
    must be able to `__init__()` without any parameters. By extension, this
    means that they need to initialize a device from scratch, using only
    env-vars. Most devices speak some dialect of SCPI (with differing transport
    layers), and for all SCPI we use EMMI's `MagicScpi`. So here's a wrapper
    to do it uniformly...

    Args:
        env: the env-var dictionary to use. If `None`, `os.environ` is used.
          These are the vars we react to:
          - `OSZI_SCPI_DEV`: SCPI device specification, e.g. `"TPCPIP::host::INSTR"`.
            There is no default to this, this is mandatory.
          - `OSZI_SCPI_HOST=<host>[:<port>]`: if `OSZI_SCPI_DEV` is not specified,
            then here a hostname (and optionally a port) can be specified. This is
            ignored if `OSCI_SCPI_DEV` is specified. If the port is not specified,
            then `::INSTR` is used as a device type suffix, which means that connection
            to port 5025 (typical SCPI VISA port) is attempted. Otherwise
            a `TCPIP::<host>::<port>::SOCKET` address is constructed.
          - `OSZI_SCPI_RMAN`: Resource manager to use, e.g. `"@py"` (this is also
            the default resource manager we're using).
         -  `OSZI_SCPI_ARGS=<key>=<value>[:<key2>=<value2>[:...]]`: configuration
            parameters to pass to the device.
    
        default_args: if this is not `None`, it's expected to be a dictionary which
          contains default args (in the sense of `OSZI_SCPI_ARGS`). The user can
          still override these through the env-var.
    
    Returns: an EMMI  `MagicScpi` object ready to use. Does NOT attempt to communicate
      with the device, or validate it in any way.
    '''

    if env is None:
        env = {}
        env.update(environ)

    if log is None:
        log = logger

    try:
        dev = env['OSZI_SCPI_DEV']
    except KeyError:
        hspec = env['OSZI_SCPI_HOST'].split(':')
        if len(hspec) == 1:
            dev = f'TCPIP::{hspec[0]}::INSTR'
        elif len(hspec) == 2:
            dev = f'TCPIP::{hspec[0]}::{hspec[1]}::SOCKET'
        else:
            raise RuntimeError(f'OSZI_SCPI_HOST must be <host>[:<port>]')

    rman = env.get('OSZI_SCPI_RMAN', '@py')
    log.info(f'Using device: {dev}, with: {rman}')

    params = env.get('OSZI_SCPI_ARGS', '')
    plist = params.split(':')
    
    argmap = {k:v for k,v in default_args.items()} \
        if default_args is not None else {}
    
    for p in plist:
        if len(p) == 0:
            continue
        kv = p.split('=')
        if len(kv) != 2:
            raise RuntimeError(f'OSZI_SCPI_ARGS: don\'t know how to parse '
                               f'"{p}" from "{params}"')
        argmap[kv[0]] = kv[1]

    log.info(f'SCPI args: {argmap}')

    return MagicScpi(device=dev, resource_manager=rman, device_conf=argmap)
