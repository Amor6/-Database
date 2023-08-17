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

    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество вакансий у каждой компании."""
        curs = self.connect.cursor()
        curs.execute("""
            SELECT company_name, COUNT(*) AS vacancies_count 
            FROM vacancies 
            GROUP BY company_name;
        """)
        result = curs.fetchall()
        curs.close()
        return result

