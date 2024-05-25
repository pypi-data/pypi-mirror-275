from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from web3 import Account

from walletconstructor.security.config import FileFormatDatabase



class GenerateKey:
    def __init__(self, name:str, password:bytes) -> None:
        self.__name = name
        self.__password = password

    def __new_key(self):
        try:
            private_key = ec.generate_private_key(ec.SECP256R1())
            pem = private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.BestAvailableEncryption(
                    self.__password))
            FileFormatDatabase(f"{self.__name}.pem", pem).write()
            return private_key
        except:
            raise
    
    @property
    def newkey(self):
        return self.__new_key()
    
class LoadKey:
    def __init__(self, name:str, password:bytes) -> None:
        self.__name = name
        self.__password = password

    def __import_key(self):
        try:
            brut_key = FileFormatDatabase(f"{self.__name}.pem", None).read()
            private_key = serialization.load_pem_private_key(
                brut_key,
                password=self.__password)
            return private_key
        except:
            raise

    @property
    def import_key(self):
        return self.__import_key()
    

class LoadKeySecurity:
    def __init__(self, name:str, password:str) -> None:
        self.__name = name
        self.__password = password.encode()
        self.__private_key = self.__connect()
        self.__private_key_hex, self.__public_key_hex = self.__keys_to_hex()

    def __connect(self):
        try:
            private_key = GenerateKey(self.__name, self.__password).newkey
        except FileExistsError:
            private_key = LoadKey(self.__name, self.__password).import_key
        except:
            raise
        finally:
            return private_key
        
    def __keys_to_hex(self):
        private_key = self.__private_key.private_numbers(             
        ).private_value.to_bytes(32,"big").hex()
        public_key = self.__private_key.public_key().public_bytes(
            encoding=serialization.Encoding.X962,
            format=serialization.PublicFormat.UncompressedPoint).hex()
        return private_key, public_key
    
    @property
    def private_key(self):
        return self.__private_key
    
    @property
    def private_key_hex(self):
        return self.__private_key_hex
    
    @property
    def public_key_hex(self):
        return self.__public_key_hex
    


class LoadPrivateKey:
    @staticmethod
    def load_key(**kwargs):
        if "private_key" in kwargs:
            return kwargs['private_key']
        elif "password" in kwargs and "name" in kwargs:
            private_key = LoadKeySecurity(kwargs['name'], kwargs['password'])
            return private_key.private_key_hex
        else:
            raise Exception("Aucune private key detecter")
        
class Security:
    def __init__(self, **kwargs) -> None:
        self.kwargs = kwargs
        self.__private_key = LoadPrivateKey.load_key(**kwargs)
        self.__account = None
        self.__connect_profile()

    def __connect_profile(self) -> None:
        account = Account.from_key(self.__private_key)
        self.__account = account

    @property
    def account(self):
        return self.__account
    
    @property
    def addr_ethereum(self):
        return self.__account.address
    
    @property
    def private_key(self):
        return self.__private_key
    
    @property
    def sign_transaction(self):
        return self.__account.sign_transaction
    
    @property
    def format_frame(self):
        return {
            "NAME": self.kwargs.get('name') or "unknown",
            "ADDR": self.addr_ethereum
        }
    