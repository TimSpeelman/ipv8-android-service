from asyncio import all_tasks, ensure_future, gather, get_event_loop, sleep
from ow_service import OpenWalletService
import argparse
import logging
import os
import sqlite3
import sys


class OpenWalletAndroidService(object):

    def __init__(self):
        '''
        Setup environment
        '''
        os.environ['PYTHON_EGG_CACHE'] = os.path.realpath(
            os.path.join(os.getenv('ANDROID_PRIVATE'), '../cache'))

        # Set logging format and level
        logging.basicConfig(
            format='%(levelname)s:%(message)s', level=logging.DEBUG)

    def run(self):
        print("OpenWalletService run xoxo")
        logging.warning("OpenWalletService run xoxo warn")
        parser = argparse.ArgumentParser(add_help=False, description=('Starts OpenWallet as a service'))
        parser.add_argument('--help', '-h', action='help', default=argparse.SUPPRESS, help='Show this help message and exit')
        parser.add_argument('--port', '-p', action='store', type=int, default=8642, help='Port number')
        parser.add_argument('--workdir', '-w', action='store', default='temp', help='The working directory')
        parser.add_argument('--fresh', '-f', action='store_true', help='Refresh the identity')
        parser.add_argument('--loglevel', '-l', action='store', default='ERROR', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], help='The log level')

        args = parser.parse_args(sys.argv[1:])

        print("OpenWalletService using arguments:")
        print(args)

        service = OpenWalletService()
        loop = get_event_loop()
        coro = service.start(args)
        ensure_future(coro)

        if sys.platform == 'win32':
            # Unfortunately, this is needed on Windows for Ctrl+C to work consistently.
            # Should no longer be needed in Python 3.8.
            async def wakeup():
                while True:
                    await sleep(1)
            ensure_future(wakeup())

        loop.run_forever()


if __name__ == '__main__':
    OpenWalletAndroidService().run()
