import sqlite3
from abc import ABC, abstractmethod
import os
from fh.path_manager import PathManager

class BaseDB(ABC):
    def __init__(self, db_file):
        path = PathManager().get_storage_path(f"{db_file}.db")
        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()
        self._create_table()

    @abstractmethod
    def _create_table(self):
        pass

    def close(self):
        self.conn.close()
