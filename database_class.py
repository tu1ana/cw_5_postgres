import psycopg2

from config import config


class DBManager:
    """Класс для работы с данными в БД; подключается к БД PostgreSQL."""

    def __init__(self, db_name, params) -> None:
        self.db_name = db_name
        self.params = params

    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество вакансий у каждой компании."""
        params = config()
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute('''SELECT employer_name, COUNT(job_id) FROM employers
                        LEFT JOIN jobs USING(employer_id)
                        GROUP BY employer_name''')
                result = cur.fetchall()
        return result

    def get_all_vacancies(self) -> list:
        """
        Получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию.
        """
        params = config()
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute('''SELECT employer_name, job_title, salary_from, salary_to, jobs.url 
                                    FROM employers
                                    INNER JOIN jobs USING(employer_id)''')
                result = cur.fetchall()
        return result

    def get_avg_salary(self) -> float:
        """Получает среднюю зарплату по вакансиям."""
        params = config()
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute('''SELECT AVG((salary_from + salary_to) / 2)
                                        FROM jobs''')
                result = float(cur.fetchone()[0])
        return result

    def get_vacancies_with_higher_salary(self) -> list:
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        params = config()
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                average_salary = self.get_avg_salary()
                cur.execute('''SELECT job_title, salary_from, salary_to, jobs.url
                                        FROM jobs
                                        WHERE salary_to > %s''', (average_salary,))
                result = cur.fetchall()
        return result

    def get_vacancies_with_keyword(self, keyword) -> list:
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python."""
        params = config()
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute('''SELECT employer_name, job_title, salary_from, salary_to, jobs.url
                                        FROM employers
                                        INNER JOIN jobs USING(employer_id)
                                        WHERE job_title ILIKE %s''', ('%' + keyword + '%',))
                result = cur.fetchall()
        return result


# db = DBManager('headhunter', params=config())
# print(db.get_companies_and_vacancies_count())
# print(db.get_all_vacancies())
# print(db.get_avg_salary())
# print(db.get_vacancies_with_higher_salary())
# print(db.get_vacancies_with_keyword('Python'))
