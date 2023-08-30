import os

from database_class import DBManager


def main():

    db_manger = DBManager(host='localhost', database='headhunter', user='postgres', password=os.getenv('DATABASE_PASS'))

    print('Список компаний с сайта hh.ru, доступных для просмотра:\n'
          'BI.ZONE\n'
          'ANABAR\n'
          'Blue underlined link\n'
          'Brand Analytics\n'
          'ФАУ ГосНИИ Авиационных Систем\n'
          'ООО Учкнига\n'
          'Mediascope\n'
          'Pacific.agency\n'
          'АО ОКБ (Объединенное Кредитное Бюро)\n'
          'BostonGene Technologies\n'
          'ООО ПроКомплаенс')
    print()

    user_input = input('Выберите вариант:\n'
                       '1 - Посмотреть количество вакансий всех компаний\n'
                       '2 - Посмотреть все вакансии\n'
                       '3 - Средняя зарплата по вакансиям\n'
                       '4 - Посмотреть вакансии с зарплатой выше средней\n'
                       '5 - Посмотреть вакансии по ключевому слову\n')
    if user_input == 1:
        job_count_total = db_manger.get_companies_and_vacancies_count()
        print(job_count_total)
    elif user_input == 2:
        all_jobs = db_manger.get_all_vacancies()
        print(all_jobs)
    elif user_input == 3:
        average_salary = db_manger.get_avg_salary()
        print(average_salary)
    elif user_input == 4:
        with_higher_salary = db_manger.get_vacancies_with_higher_salary()
        print(with_higher_salary)
    elif user_input == 5:
        user_input = input('Введите ключевое слово: ')
        with_keyword = db_manger.get_vacancies_with_keyword(user_input)
        print(with_keyword)
    else:
        print('Что-то пошло не так, попробуйте ещё раз')


if __name__ == '__main__':
    main()
