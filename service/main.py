import logging
import os
import sqlite3


class OpenWalletService(object):

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




if __name__ == '__main__':
    OpenWalletService().run()
