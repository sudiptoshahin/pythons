import os
from pathlib import Path
class Logger(object):
    _instance = None
    _file_name = None

    """
        * __new__ is called before __init__ 
        * __new__  is a static method and creating new instance
        * __init__ is initializes the instance after it is created
    """
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance
    
    def _initialize(self) -> None:
        if self._file_name is None:
            log_dir: str = os.path.join(os.getcwd(), "log")
            os.makedirs(log_dir, exist_ok=True)
            temp_log_file: str = os.path.join(log_dir, "test_log.log")
            self._file_name = Path(temp_log_file)
            if not self._file_name.exists():
                with open(self._file_name, "x", encoding="utf-8") as file:
                    print(file)


    def __init__(self) -> None:
        self._initialize()

    def _write_log(self, level: str, msg: str)-> None:
        print(f'path: {self._file_name}')
        with open(self._file_name, "a", encoding="utf-8") as log_file:
            log_file.write(f"\n[{level}] {msg}")

    def critical(self, msg:str)-> None:
        """cricitical"""
        self._write_log("CRITICAL", msg)

    def error(self, msg: str)-> None:
        """error"""
        self._write_log("ERROR", msg)

    def warn(self, msg: str)-> None:
        """warn"""
        self._write_log("WARN", msg)
    def debug(self, msg: str)-> None:
        """debug"""
        self._write_log("DEBUG", msg)
    def info(self, msg: str)-> None:
        """info"""
        self._write_log("INFO", msg)

if __name__ == "__main__":
    l1 = Logger()
    l2 = Logger()

    l1.error("Hello world")
    l2.critical("This is very critical situation.")

    print(f"l1: {l1}")
    print(f"l2: {l2}")