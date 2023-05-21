from user_pass import DatabaseLocalLoginInfo
# import other classes from user_pass.py

from sqlalchemy import create_engine
from urllib.parse import quote_plus
import mysql.connector
from mysql.connector import Error


class DatabaseEngine:
    def __init__(self):
        self.engine = None
        self.database_login = DatabaseLocalLoginInfo()
        self.username = self.database_login.username
        self.password = self.database_login.password
        self.host = self.database_login.host
        self.port = self.database_login.port
        self.database = "your_database_name"
        self.create_database()
        self.connection = None

    def create_database(self):
        connection = mysql.connector.connect(host=self.host,
                                             user=self.username,
                                             password=self.password,
                                             port=self.port)
        cursor = connection.cursor()
        cursor.execute("""CREATE DATABASE
        IF
        NOT EXISTS {} CHARACTER 
        SET utf8mb4 COLLATE utf8mb4_unicode_ci;""".format(self.database))

        cursor.close()
        connection.close()

    def get_engine(self):
        engine = create_engine('mysql+mysqlconnector://{0}:{1}@{2}:{3}/{4}'.format(quote_plus(self.username),
                                                                                   quote_plus(self.password),
                                                                                   self.host,
                                                                                   self.port,
                                                                                   self.database),
                               echo=False)
        print("hello")
        self.engine = engine
        return engine

    def get_cursor(self):
        connection = mysql.connector.connect(host=self.host,
                                             database=self.database,
                                             user=self.username,
                                             password=self.password,
                                             port=self.port)

        return connection