Курсовая работа №5
----------------------------------------------------------------
Проект собирает данные по 10 компаниям и размещённым ими вакансиям по API hh.ru; подключается к БД PostgreSQL, создаёт таблицы с работодателями и вакансиями.

Чтобы запустить проект, клонируйте этот репозиторий на свой компьютер, установите зависимости командой `poetry install`, 
создайте базу данных в PostgreSQL, укажите свои параметры для подключения к БД в файле `database.ini`:

|[postgresql]  |
|---|
|host=_hostname_ |
|database=_database_name_ |
|user=_username_ |
|password=_your_password_ |
|port=_port_number_ |
запустите файл `utils.py`, который подключится к БД, создаст таблицы и заполнит их данными; далее запустите файл `main.py`.

Основные функции проекта, позволяющие получать:
*  список всех компаний и количество вакансий у каждой компании;
*  список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию;
*  среднюю зарплату по вакансиям;
*  список всех вакансий, у которых зарплата выше средней по всем вакансиям;
*  список всех вакансий, в названии которых содержатся переданные в метод слова, например, python.
