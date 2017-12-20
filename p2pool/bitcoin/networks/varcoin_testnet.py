import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = '152b1959'.decode('hex')
P2P_PORT = 29333
ADDRESS_VERSION = 111
RPC_PORT = 29332
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'bitcoinaddress' in (yield bitcoind.rpc_help()) and
            (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 21000000 * 100000000 if height == 1 else (50*100000000 >> (height + 1)//420000)
POW_FUNC = data.hash256
BLOCK_PERIOD = 600 # s
SYMBOL = 'tVAR'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Varcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Varcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.varcoin'), 'varcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://blockexplorer.com/testnet/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://blockexplorer.com/testnet/address/'
TX_EXPLORER_URL_PREFIX = 'http://blockexplorer.com/testnet/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000 - 1, 2**256//2**32 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 1e8
