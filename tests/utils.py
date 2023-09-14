from substrateinterface import Keypair

PARACHAIN_WS_URL = 'ws://127.0.0.1:10044'
URI_GLOBAL_SUDO = '//Alice'
KP_GLOBAL_SUDO = Keypair.create_from_uri(URI_GLOBAL_SUDO)
