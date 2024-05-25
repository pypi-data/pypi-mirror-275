from pathlib import Path
import json



class ConfigEnv:
    path_dirname = ".key_database"
    @staticmethod
    def path_database() -> Path:
        return Path(__file__).parent.parent / ConfigEnv.path_dirname
    @staticmethod
    def set_path_dirname(path:str) -> None:
        ConfigEnv.path_dirname = path
    

class ConfigDatabase:
    def __init__(self) -> None:
        self._path = ConfigEnv.path_database()
        self.__connect_database()

    def __connect_database(self) -> None:
        try:
            if not self._path.exists():
                self._path.mkdir(exist_ok=True)
                return None
            return None
        except:
            raise

class FileFormatDatabase:
    def __init__(self, filename:str, data) -> None:
        self.__filename_no_formated = filename
        self.__data = data
        self.__filename_formated = None
        self.__connect_format_file()

    def __connect_format_file(self) -> None:
        filename = ConfigEnv.path_database().joinpath(self.__filename_no_formated)
        self.__filename_formated = filename
        return None
    
    def write(self) -> None:
        try:
            if self.__filename_formated.exists():
                raise FileExistsError(
                    f"Le fichier existe déjà {self.__filename_no_formated}")
            with open(self.__filename_formated, 'wb') as f:
                f.write(self.__data)
            return None
        except:
            raise

    def read(self):
        if self.__filename_formated.exists():
            with open(self.__filename_formated, 'rb') as f:
                return f.read()
        raise FileNotFoundError(
            f"Le fichier {self.__filename_formated} n'existe pas")
    

class ConfigProvider:
    LOCALHOST = "http://127.0.0.1:7545"

config_db = ConfigDatabase()
