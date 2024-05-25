from web3 import Web3
from web3.exceptions import ProviderConnectionError, TransactionNotFound, InvalidAddress, Web3ValidationError, ContractLogicError, Web3Exception
from walletconstructor.wallet.infos.infos import Infos
from walletconstructor.wallet.walletutils import WalletUtils
from walletconstructor.wallet.transactionwallet import TransactionHistory
from walletconstructor.wallet.tokens import TokenContract, Tokens
from walletconstructor.security.security import Security
from decimal import Decimal
from typing import Literal, Dict, Any

class Wallet:
    def __init__(self, security_wallet: Security, http_provider: str) -> None:
        self.security = security_wallet
        self._http_provider = http_provider
        self.web3 = None
        self.infos = None
        self.transactions = None
        self.tokens = None
        self.__connect()

    def __connect(self) -> None:
        try:
            self.web3 = Web3(Web3.HTTPProvider(self._http_provider))
            if not self.web3.is_connected():
                raise ProviderConnectionError("Aucun provider valide")
            self.transactions = TransactionHistory(self.web3)
            self.tokens = Tokens(self.web3, self.security)
            self.infos = Infos(self.web3, self.security, self.tokens)
        except (ProviderConnectionError, Web3Exception, Exception) as e:
            raise ProviderConnectionError("Erreur de connexion à la blockchain") from e

    def add_token(self, addr:str, abi:dict) -> None:
        self.tokens.add_token(addr, abi, self.infos)
        self.infos.update_infos()
    

    def send(self, to: str, value: Decimal, speed: Literal['fast', 'average', 'slow'] = 'fast') -> Dict[str, Any]:
        try:
            res = WalletUtils.build_transaction(
                self.web3,
                self.security,
                to,
                value,
                speed
            )
            self.transactions._wait_transaction(res)
            self.infos.update_infos()
            return {
                'build_transaction': res['build_transaction'],
                'speed': speed,
                'transaction_receipt': self.transactions.history[res['hash_transaction']]
            }
        except (TransactionNotFound, InvalidAddress, Web3ValidationError, ContractLogicError, Web3Exception) as e:
            raise Exception("Erreur lors de l'envoi de la transaction") from e

    def estimate_gas_cost(self, to: str, value: Decimal, speed: Literal['fast', 'average', 'slow'] = 'fast') -> Dict[str, Decimal]:
        try:
            gas_price = WalletUtils.get_gas_price(self.web3, speed)
            gas_limit = WalletUtils.get_gas_limit(self.web3, self.security, to, value)
            gas_cost_eth = gas_price * gas_limit
            gas_cost_eth = self.web3.from_wei(gas_cost_eth, 'ether')
            
            # Obtenir les prix de l'ether en BTC, USD et EUR depuis Infos
            ether_price = self.infos.ether_price
            
            gas_cost_btc = gas_cost_eth * Decimal(ether_price['BTC'])
            gas_cost_usd = gas_cost_eth * Decimal(ether_price['USD'])
            gas_cost_eur = gas_cost_eth * Decimal(ether_price['EUR'])

            return {
                'eth': gas_cost_eth,
                'btc': gas_cost_btc,
                'usd': gas_cost_usd,
                'eur': gas_cost_eur
            }
        except (TransactionNotFound, InvalidAddress, Web3ValidationError, ContractLogicError, Web3Exception) as e:
            raise Exception("Erreur lors de l'estimation du coût du gaz") from e

    def verify_addr(self, addr: str, raise_exception: bool = False) -> bool:
        try:
            if Web3.is_address(addr):
                return True
            if raise_exception:
                raise InvalidAddress("Address Invalide")
            else:
                return False
        except (Web3Exception, Exception) as e:
            raise Exception("Erreur lors de la vérification de l'adresse") from e


