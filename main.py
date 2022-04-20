import os

from dotenv import load_dotenv

from common_functions import drow_terminal_table
from hh_functions import report_vacancies_hh
from sj_functions import report_vacancies_sj

programming_languages = ['Python', 'Java']


def main():
    load_dotenv()
    sj_token = os.getenv('SJ_API_TOKEN')
    vacancies_hh = report_vacancies_hh(programming_languages)
    vacancies_sj = report_vacancies_sj(programming_languages, sj_token)
    drow_terminal_table(vacancies_hh)
    drow_terminal_table(vacancies_sj)


if __name__ == '__main__':
    main()
