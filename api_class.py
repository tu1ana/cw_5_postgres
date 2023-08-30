from pprint import pprint

import requests


class HeadHunterAPI:
    """Класс для подключения к HeadHunter, собирающий информацию по вакансиям от определённых компаний"""

    employer_list = [
        'BI.ZONE', 'ANABAR', 'Blue underlined link', 'Brand Analytics',
        'Федеральное автономное учреждение Государственный Научно-Исследовательский Институт Авиационных Систем',
        'Учкнига', 'Mediascope', 'Pacific.agency', 'ОКБ', 'BostonGene Technologies', 'ПроКомплаенс'
    ]

    def get_vacancies(self, employer: str) -> list[dict]:
        """Получаем информацию по вакансиям по заданной компании"""
        params = {
            'text': employer,
            'page': 0,
            'per_page': 100
        }
        response = requests.get('https://api.hh.ru/vacancies', params=params).json()['items']
        return response

    def get_employer_data(self, employer_list: list) -> dict:
        employer_data = {}

        for employer in employer_list:
            job_data = self.get_vacancies(employer)
            employer_data[employer] = job_data
        return employer_data


hhapi = HeadHunterAPI()
# print(hhapi.get_vacancies('ПроКомплаенс'))
pprint(hhapi.get_employer_data([
        'BI.ZONE', 'ANABAR', 'Blue underlined link', 'Brand Analytics',
        'Федеральное автономное учреждение Государственный Научно-Исследовательский Институт Авиационных Систем',
        'Учкнига', 'Mediascope', 'Pacific.agency', 'ОКБ', 'BostonGene Technologies', 'ПроКомплаенс'
    ]))
