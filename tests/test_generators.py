from src.generators import card_number, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions):
    """Тест функции filter_by_currency"""
    i = filter_by_currency(transactions, "RU")
    assert next(i) == {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount': {'amount': '79114.93', 'currency': {'name': 'RU', 'code': 'RU'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'}

def test_transaction_descriptions(transactions):
    """Тест функции transaction_descriptions"""
    i = transaction_descriptions(transactions)
    assert next(i) == "Перевод организации"
    assert next(i) == "Перевод со счета на счет"

def test_card_number():
    """Тест функции transaction_descriptions"""
    i = card_number()
    assert next(i) == "0000 0000 0000 0000"
    assert next(i) == "0000 0000 0000 0001"
    assert next(i) == "0000 0000 0000 0002"
    assert next(i) == "0000 0000 0000 0003"