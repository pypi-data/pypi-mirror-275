from walletconstructor.security.security import Security
from walletconstructor.security.config import ConfigProvider
from walletconstructor.wallet.wallet import Wallet

def get_wallet(**kwargs) -> Wallet:
    s = Security(**kwargs)
    w = Wallet(s, ConfigProvider.LOCALHOST)
    return w