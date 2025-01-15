import re

from src.utils import data_operatinons_convert
from src.file_reader import transformation_csv, transformation_excel
from src.searching import find_transactions
from src.processing import sort_by_date
from  src.generators import filter_by_currency, transaction_descriptions

def format_selection():
    while True:
        print(''' 
        Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файл''')
        namber = input()
        if namber == '1':
            return data_operatinons_convert('D:/my_project2/pythonProject1/data/operations.json')
        elif namber == '4':
            return transformation_csv('D:/my_project2/pythonProject1/data/operations.json')
        elif namber == '3':
            return transformation_excel('D:/my_project2/pythonProject1/data/operations.json')
        else:
            print('Неизвестная команда')

def statuse_selection(data_search:list[dict]) -> list[dict]:
    data_statuse_selection = []
    while True:
        print('''Введите статус, по которому необходимо выполнить фильтрацию. 
            Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING''')
        status = input()
        if re.search(status.upper(), 'EXECUTED, CANCELED, PENDING'):
            for data in data_search:
                if re.search(data.get("state",''), status.upper()) is not None:
                    data_statuse_selection.append(data)
            return data_statuse_selection
        else:
            print('Неизвестная команда')

def date_sort(data) -> list[dict]:
    while True:
        yes_no = input('Отсортировать операции по дате? Да/Нет')
        sort_welue = input('Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию')

        if yes_no.lower() == 'да' and sort_welue.lower() == 'по возрастанию':
            return sort_by_date(data)
        elif yes_no.lower() == 'да' and sort_welue.lower() == 'по убыванию':
            return sort_by_date(data, False)
        elif yes_no.lower() == 'нет':
            return data
        else:
            print('Неизвестная команда')

def main_filter_by_currency(data:list[dict]) -> list[dict]:
    rub_welue = input('Выводить только рублевые тразакции? Да/Нет')
    if rub_welue.lower() == 'да':
        data_filter_by_currency = [data for data in filter_by_currency(data, 'RUB')]
        return data_filter_by_currency
    else:
        return data

def main_find_transactions(data) -> list[dict]:
    description_yes_no = input('Отфильтровать список транзакций по определенному слову в описании? Да/Нет')
    description = input('Введите определённое слово')
    if description_yes_no.lower() == 'да':
        return find_transactions(data, description)


def main():
    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями.')
    data = format_selection()
    data_filter = statuse_selection(data)
    data_date_filter = date_sort(data_filter)
    data_date_filter = main_filter_by_currency(data_date_filter)
    data_date_filter = main_find_transactions(data_date_filter)
    print(data_date_filter)




main()