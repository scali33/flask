import sqlite3
class DataBaseConnection:
    def __init__(self,host):
        self.host = host
        self.conection = None
        pass
    def __enter__(self):
        self.conection = sqlite3.connect(self.host)
        return self.conection
    def __exit__(self, exc_type,exc_val,exc_tb):
        if exc_type or exc_val or exc_tb:
            self.conection.close()
        else:
            self.conection.commit()
            self.conection.close()