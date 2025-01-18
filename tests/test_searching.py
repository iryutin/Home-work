from src.searching import find_transactions, group_transactions_by_category


def test_find_transactions(transactions):
    assert find_transactions(transactions, "Перевод организации") == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    ]


def test_group_transactions_by_category(transactions):
    assert group_transactions_by_category(transactions, ["Перевод организации", "Перевод со счета на счет"]) == {
        "Перевод организации": 1,
        "Перевод со счета на счет": 1,
    }
