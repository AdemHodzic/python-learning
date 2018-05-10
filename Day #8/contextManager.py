import mysql.connector

class Manager:
    def __init__(self, config):
        self.configuration = config

    def __enter__(self):
        self.connection = mysql.connector.connect(**self.configuration)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self,  exc_type, exc_value, exc_trace):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()