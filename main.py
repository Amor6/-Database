from db_manager import DBManager
from api_hh_cl import HeadHunter


def main():
    dbass = DBManager()
    headh = HeadHunter()
    vacancies = headh.get_vacancies()
    dbass.info_vacancies(vacancies)

    # Получаем список компаний и количество вакансий у каждой компании
    companies_vacancies_count = dbass.get_companies_and_vacancies_count()
    print(" Информация о вакансий у компаний:")
    for row in companies_vacancies_count:
        print(row[0], "-", row[1])
  # Получение информации о компании и её вакансиях

    all_vacancies = dbass.get_all_vacancies()
    print("Список вакансий:")
    for row in all_vacancies:
        print(row)
    # Получение списка вакансий

    avg_salary = dbass.get_avg_salary()
    print("Средняя зарплата по вакансиям:", avg_salary)
    #Средняя ЗП по вакансиях

    high_salary_vacancies = dbass.get_vacancies_with_higher_salary()
    print("Вакансии с зарплатой выше средней:")
    for row in high_salary_vacancies:
        print(row[0])
    # Информация по ЗП выше средний

    keyword = "Python"
    vacancies_with_keyword = dbass.get_vacancies_with_keyword(keyword)
    print(f"Список вакансий, по запрашиваемой должности '{keyword}':")
    for row in vacancies_with_keyword:
        print(row[0], "-", row[1], "-", row[2])
    # Сортировка вакансий по запрашиваемому слову

if __name__ == '__main__':
    main()