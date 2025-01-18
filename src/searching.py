import logging
import re
from collections import Counter

logger = logging.getLogger("searching")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("D:/my_project2/pythonProject1/logs/searching.log")
file_formater = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def find_transactions(transactions_list: list[dict], key_string: str) -> list[dict]:
    """Принимает список словарей с данными о банковских операциях и строку поиска. Возвращает список словарей, у \
    которых в описании есть данная строка."""
    filtered_transactions_list = []
    for transaction in transactions_list:
        if re.search(f".*{key_string}.*", transaction["description"], flags=re.IGNORECASE) is not None:
            filtered_transactions_list.append(transaction)
    logger.info(f"Список операций успешно отфильтрован по описанию {key_string}.")
    return filtered_transactions_list


def group_transactions_by_category(transactions_list: list[dict], description_list: list) -> dict:
    """Принимает список словарей с данными о банковских операциях и список категорий операций, а возвращать словарь, \
    в котором ключи — это названия категорий, а значения — это количество операций в каждой категории."""
    new_description_list = []
    for transaction in transactions_list:
        for description in description_list:
            if re.search(transaction.get("description", ""), description) is not None:
                new_description_list.append(transaction.get("description", ""))
    grouped_transactions = Counter(new_description_list)
    logger.info("Список операций успешно сгрупирован по названиям категорий.")
    return dict(grouped_transactions)
