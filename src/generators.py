import textwrap
from email.generator import Generator



def filter_by_currency(transaction: list[dict], currency:str) -> Generator:
    """Фильтрация списка по валюте"""
    transaction_filter = (x for x in transaction if x["operationAmount"]["currency"]["code"]== currency)
    return transaction_filter




def transaction_descriptions(transaction: list[dict]) -> iter:
    """Выдача вида операции"""
    result = (x.get("description") for x in transaction)
    for x in result:
        yield x

def card_number() -> iter:
    """Генерация номера карты"""
    x = 0
    while x <= 9999999999999999:
        new_card_namber = '0'*(16-len(str(x)))+str(x)
        yield ' '.join(textwrap.wrap(new_card_namber, 4))
        x += 1
