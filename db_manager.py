import psycopg2
import os


class DBManager:
    def __init__(self):
        try:
            self.connect = psycopg2.connect(
                host="localhost",
                dbname="vacansies",
                user="postgres",
                password=os.getenv(' ')
            )
        except psycopg2.Error as e:
            print("Не удается подключиться к BD.")
            print(e)

