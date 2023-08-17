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

    def get_all_vacancies(self):

        """Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на
        вакансию."""

        curs = self.connect.cursor()
        curs.execute("""
            SELECT * 
            FROM vacancies;
        """)
        result = curs.fetchall()
        curs.close()
        return result

    def get_avg_salary(self):
        """Получает среднюю зарплату по вакансиям"""
        curs = self.connect.cursor()
        curs.execute("""
            SELECT AVG(salary) 
            FROM vacancies;
        """)
        result = curs.fetchone()[0]
        curs.close()
        return result


