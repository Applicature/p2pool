import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = '2c1a6018'.decode('hex')
P2P_PORT = 28333
ADDRESS_VERSION = 0
RPC_PORT = 28332
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            (yield helper.check_genesis_block(bitcoind, '0000000013d13169397663f35a34cc381592eb6cfd2e099331bc559c44f80e68')) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 21000000 * 100000000 if height == 1 else (50*100000000 >> (height + 1)//420000)

POW_FUNC = data.hash256
BLOCK_PERIOD = 600 # s
SYMBOL = 'VAR'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Varcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Varcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.varcoin'), 'varcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://blockchain.info/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'https://blockchain.info/address/'
TX_EXPLORER_URL_PREFIX = 'https://blockchain.info/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.001e8
