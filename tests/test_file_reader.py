from unittest.mock import patch

import pandas as pd

from src.file_reader import transformation_csv, transformation_excel


@patch("pandas.read_csv")
def test_transformation_csv(mock_get):
    """Тест функции transformation_csv"""
    mock_get.return_value = pd.DataFrame(
        {
            "id": 441945886,
            "state": ["EXECUTED"],
            "date": ["2019-08-26T10:50:58.294041"],
            "amount": ["31957.58"],
            "currency_name": ["руб."],
            "currency_code": ["RUB"],
            "description": ["Перевод организации"],
            "from": ["Maestro 1596837868705199"],
            "to": ["Счет 64686473678894779589"],
        }
    )
    assert transformation_csv("") == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ]


@patch("pandas.read_excel")
def test_transformation_exel(mock_get):
    """Тест функции transformation_csv"""
    mock_get.return_value = pd.DataFrame(
        {
            "id": 441945886,
            "state": ["EXECUTED"],
            "date": ["2019-08-26T10:50:58.294041"],
            "amount": ["31957.58"],
            "currency_name": ["руб."],
            "currency_code": ["RUB"],
            "description": ["Перевод организации"],
            "from": ["Maestro 1596837868705199"],
            "to": ["Счет 64686473678894779589"],
        }
    )
    assert transformation_excel("") == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ]
