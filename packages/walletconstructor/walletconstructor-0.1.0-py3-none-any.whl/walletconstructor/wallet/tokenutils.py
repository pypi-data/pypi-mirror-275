from web3 import Web3
from web3.contract import Contract
from walletconstructor.security.security import Security
from decimal import Decimal
from typing import Literal, Dict, Any
from walletconstructor.wallet.walletutils import WalletUtils as wu

class TokenUtils:

    @staticmethod
    def estimate_gas_for_buy(
        contract: Contract, 
        addr: str, 
        value: Decimal, 
        nonce: int
    ) -> int:
        # Convertir la valeur en Wei
        value_in_wei = Web3.to_wei(value, 'ether')
        return contract.functions.buyTokens().estimate_gas({'from': addr, 'value': value_in_wei, 'nonce': nonce})

    @staticmethod
    def estimate_gas_for_sell(
        contract: Contract, 
        addr: str, 
        value: Decimal
    ) -> int:
        return contract.functions.sellTokens(int(value)).estimate_gas({'from': addr})

    @staticmethod
    def estimate_gas_for_transfer(
        contract: Contract, 
        addr: str, 
        to: str, 
        value: Decimal
    ) -> int:
        return contract.functions.transfer(to, int(value)).estimate_gas({'from': addr})

    @staticmethod
    def build_tx(_from: str, **kwargs) -> dict:
        kwargs['from'] = _from
        return kwargs

    @staticmethod
    def build_transaction_buy_tokens(
        web3: Web3,
        contract: Contract,
        security: Security,
        value: Decimal,
        speed: Literal['fast', 'average', 'slow'] = 'fast',
    ) -> dict:
        # Convertir la valeur en Wei
        value_in_wei = Web3.to_wei(value, 'ether')
        
        gas_price = wu.get_gas_price(web3, speed)
        nonce = wu.get_nonce(web3, security)
        gas_limit = TokenUtils.estimate_gas_for_buy(
            contract, 
            security.addr_ethereum,
            value_in_wei,
            nonce)
        
        tx_params = TokenUtils.build_tx(
            _from=security.addr_ethereum,
            nonce=nonce,
            gas=gas_limit,
            value=value_in_wei,
            gasPrice=gas_price,
            chainId=web3.eth.chain_id)
        tx = contract.functions.buyTokens().build_transaction(tx_params)
        signed_tx = wu.sign_transaction(security, tx)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        response = {
            "hash_transaction": tx_hash,
            "build_transaction": tx_params,
        }
        return response

    @staticmethod
    def build_transaction_sell_tokens(
        web3: Web3,
        contract: Contract,
        security: Security,
        amount: Decimal,
        speed: Literal['fast', 'average', 'slow'] = 'fast'
    ) -> dict:
        try:
            
            nonce = wu.get_nonce(web3, security)
            gas_limit = TokenUtils.estimate_gas_for_sell(contract, security.addr_ethereum, amount)
            gas_price = wu.get_gas_price(web3, speed)
            tx_params = TokenUtils.build_tx(
                _from=security.addr_ethereum,
                nonce=nonce,
                gas=gas_limit,
                gasPrice=gas_price,
                chainId=web3.eth.chain_id)
            tx = contract.functions.sellTokens(int(amount)).build_transaction(tx_params)
            signed_tx = wu.sign_transaction(security, tx)
            tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            response = {
                'hash_transaction': tx_hash,
                "build_transaction": tx_params
            }
            return response
        except:
            raise

    @staticmethod
    def build_transfer_token(
        web3: Web3,
        contract: Contract,
        security: Security,
        to: str,
        amount: Decimal,
        speed: Literal['fast', 'average', 'slow'] = 'fast'
    ) -> dict:
        
        nonce = wu.get_nonce(web3, security)
        gas_limit = TokenUtils.estimate_gas_for_transfer(
            contract,
            security.addr_ethereum,
            to,
            amount)
        gas_price = wu.get_gas_price(web3, speed)
        tx_params = TokenUtils.build_tx(
            _from=security.addr_ethereum,
            nonce=nonce,
            gas=gas_limit,
            gasPrice=gas_price,
            chainId=web3.eth.chain_id)
        tx = contract.functions.transfer(to, int(amount)).build_transaction(tx_params)
        signed_tx = wu.sign_transaction(security, tx)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return {
            'hash_transaction': tx_hash,
            "build_transaction": tx_params
        }
