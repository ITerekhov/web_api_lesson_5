from terminaltables import AsciiTable


def predict_salary(salary_from, salary_to):
    if all([bool(salary_from), bool(salary_to)]):
        return int((salary_from + salary_to) // 2)
    elif bool(salary_from):
        return int(salary_from * 1.2)
    elif bool(salary_to):
        return int(salary_to * 0.8)
    return None


def drow_terminal_table(report_vacancies: dict):
    serialised_data = [['Язык программирования', 'Вакансий найдено',
                       'Вакансий обработано', 'Средняя зарплата']]
    for language, details in report_vacancies['items'].items():
        serialised_data.append((language, *[i for i in details.values()]))
    table = AsciiTable(serialised_data)
    table.title = f"{report_vacancies['service']} {report_vacancies['city']}"
    print(table.table)
