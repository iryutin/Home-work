import textwrap
from collections.abc import Iterator


def filter_by_currency(transaction: list[dict], currency: str) -> Iterator:
    """Фильтрация списка по валюте"""
    transaction_filter = (x for x in transaction if x["operationAmount"]["currency"]["code"] == currency)
    return transaction_filter


def transaction_descriptions(transaction: list[dict]) -> Iterator:
    """Выдача вида операции"""
    result = (x.get("description") for x in transaction)
    for x in result:
        yield x


def card_number() -> Iterator:
    """Генерация номера карты"""
    x = 0
    while x <= 9999999999999999:
        new_card_namber = "0" * (16 - len(str(x))) + str(x)
        yield " ".join(textwrap.wrap(new_card_namber, 4))
        x += 1
