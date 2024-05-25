from walletconstructor.wallet.contract import TokenContract
from web3 import Web3
from walletconstructor.security.security import Security
from typing import Any, Dict

class Tokens(dict):
    def __init__(self, web3: Web3, security: Security, *args: Any, **kwargs: Any) -> None:
        self._web3 = web3
        self._security = security
        super().__init__(*args, **kwargs)

    def add_token(self, addr: str, abi: Dict[str, Any], wallet_infos) -> None:
        try:
            contract = TokenContract(self._web3, addr, abi, wallet_infos)
            self[contract.name] = contract
        except Exception as e:
            raise Exception(f"Erreur lors de l'ajout du token : {e}")

    def __getitem__(self, key: Any) -> TokenContract:
        if key in self:
            return super().__getitem__(key)
        raise KeyError(f"Token '{key}' non trouvé")

    def get(self, key: Any, default: Any = None) -> TokenContract:
        return super().get(key, default)
