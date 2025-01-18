import re

from src.utils import data_operatinons_convert
from src.file_reader import transformation_csv, transformation_excel
from src.searching import find_transactions
from src.processing import sort_by_date, filter_by_state
from  src.generators import filter_by_currency
from src.widget import mask_account_card

def format_selection() -> list[dict]:
    while True:
        print(''' 
        Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файл''')
        namber = input()
        if namber == '1':
            return data_operatinons_convert('data/operations.json')
        elif namber == '2':
            return transformation_csv('data/transactions.csv')
        elif namber == '3':
            return transformation_excel('data/transactions_excel.xlsx')
        else:
            print('Неизвестная команда')

def main_filter_by_state(data_search:list[dict]) -> list[dict]:
    while True:
        print('''Введите статус, по которому необходимо выполнить фильтрацию. 
            Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING''')
        status = input()
        if re.search(status.upper(), 'EXECUTED, CANCELED, PENDING'):
            return filter_by_state(data_search, status)
        else:
            print('Неизвестная команда')

def main_sort_by_date(data:list[dict]) -> list[dict]:
    while True:
        yes_no = input('Отсортировать операции по дате? Да/Нет')
        if yes_no.lower() == 'да':
            sort_welue = input('Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию')
            if sort_welue.lower() == 'по возрастанию':
                return sort_by_date(data)
            elif sort_welue.lower() == 'по убыванию':
                return sort_by_date(data, False)
            else:
                print('Неизвестная команда')
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

def main_find_transactions(data:list[dict]) -> list[dict]:
    description_yes_no = input('Отфильтровать список транзакций по определенному слову в описании? Да/Нет')
    if description_yes_no.lower() == 'да':
        description = input('Введите определённое слово')
        return find_transactions(data, description)
    else:
        return data


def main():
    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями.')
    data = format_selection()
    data_filter = main_filter_by_state(data)
    data_date_filter = main_sort_by_date(data_filter)
    data_date_filter = main_filter_by_currency(data_date_filter)
    data_date_filter = main_find_transactions(data_date_filter)
    print('Распечатываю итоговый список транзакций...')
    print(f'Всего банковских операций в выборке: {len(data_date_filter)}')
    for data in data_date_filter:
        if len(data_date_filter) == 0:
            print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')
        else:
            print(f'{data['date']} {data['description']}')
            if data['description'].lower() == 'открытие вклада':
                print(
                    f'{mask_account_card(data['to'])}\nСумма: {data['operationAmount']['amount']} {data['operationAmount']['currency']['code']}')
            else:
                print(
                    f'{mask_account_card(data['from'])} -> {mask_account_card(data['to'])}\nСумма: {data['operationAmount']['amount']}{data['operationAmount']['currency']['code']}')
