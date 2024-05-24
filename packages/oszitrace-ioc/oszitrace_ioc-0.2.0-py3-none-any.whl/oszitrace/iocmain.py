#!/usr/bin/python3

import logging, os, asyncio, sys
logger = logging.getLogger("oszitrace")

from oszitrace.iocapp import OsziIocApplication

def init_ioc(args, env):
    app = OsziIocApplication(args or sys.argv, env or os.environ)
    return app


def run_ioc(args=None, env=None):
    logging.basicConfig()
    logger.setLevel(logging.INFO)
    
    app = init_ioc(args or sys.argv, env or os.environ)
    asyncio.run(app.run())

if __name__ == "__main__":
    run_ioc(sys.argv, os.environ)
