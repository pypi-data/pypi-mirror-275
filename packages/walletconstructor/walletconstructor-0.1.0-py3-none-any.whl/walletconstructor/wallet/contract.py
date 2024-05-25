from web3.contract import Contract 
from web3 import Web3
from walletconstructor.security.security import Security
from typing import Any, Literal
from decimal import Decimal
from walletconstructor.wallet.tokenutils import TokenUtils as tu
from walletconstructor.wallet.transactiontoken import TransactionHistory

class TokenContract:
    def __init__(
            self,
            wallet_provider:Web3,
            addr_contract:str, 
            abi_contract:dict,
            wallet_infos
            ) -> None:
        self._web3 = wallet_provider
        self._addr_contract= addr_contract
        self._abi_contract = abi_contract 
        self.contract = self.__connect_contract()
        self.__name, self.__symbol = self.__connect_infos()
        self.transactions = TransactionHistory(self._web3)
        self._infos_wallet = wallet_infos

    @property
    def name(self) -> str:
        return self.__name
    @property
    def symbol(self) -> str:
        return self.__symbol
    def __connect_infos(self) -> tuple:
        try:
            name = self.contract.functions.name().call()
            symbol = self.contract.functions.symbol().call()
            return name, symbol
        except:
            raise

    def __connect_contract(self) -> Contract:
        try:
            return self._web3.eth.contract(
                address=self._web3.to_checksum_address(
                    self._addr_contract),
                    abi=self._abi_contract)
        except Exception as e:
            raise Exception(f"Erreur de connexion du contrat: {e}")
        
        
    def balance(self, security: Security) -> Decimal:
        return Decimal(self.contract.functions.balanceOf(security.addr_ethereum).call())
    
    
    def token_price(self) -> Decimal:
        token_price = self.contract.functions.tokenPrice().call()
        token_price = self._web3.from_wei(token_price,'ether')
        token_per_ether = self.contract.functions.tokensPerEther().call()
        result = token_price / token_per_ether
        return Decimal(result)
    
    def total_supply(self) -> int:
        return self.contract.functions.totalSupply().call()
    

    def buy_tokens(self, security:Security, ether_amount:Decimal, speed:Literal['fast', 'average', 'slow']):
        try:
            res = tu.build_transaction_buy_tokens(
                self._web3,
                self.contract,
                security,
                ether_amount,
                speed)
            self.transactions._wait_transaction(res)
            self._infos_wallet.update_infos()
            return {
                'build_transaction': res['build_transaction'],
                'speed': speed,
                'transaction_receipt': self.transactions.history[res['hash_transaction']]
            } 
        except:
            raise

    def sell_tokens(self, security:Security, amount_token:Decimal, speed:Literal['fast', 'average', 'slow']):
        try:
            res = tu.build_transaction_sell_tokens(
                self._web3,
                self.contract,
                security,
                amount_token,
                speed)
            self.transactions._wait_transaction(res)
            self._infos_wallet.update_infos()
            return {
                'build_transaction': res['build_transaction'],
                'speed': speed,
                'transaction_receipt': self.transactions.history[res['hash_transaction']]
            }
        except:
            raise

    def transfer(self, security:Security, amount_token:Decimal, to:str, speed:Literal['fast', 'average', 'slow']):
        try:
            res = tu.build_transfer_token(
                self._web3,
                self.contract,
                security,
                to,
                amount_token,
                'fast')
            self.transactions._wait_transaction(res)
            self._infos_wallet.update_infos()
            return {
                'build_transaction': res['build_transaction'],
                'speed': speed,
                'transaction_receipt': self.transactions.history[res['hash_transaction']]
            }
        except:
            raise