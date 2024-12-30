import os

import requests
from dotenv import load_dotenv

load_dotenv()


def currency_conversion(operation_data: dict) -> float:
    """Конвертация валюты через API"""
    if operation_data["operationAmount"]["currency"]["code"] == "RUB":
        return float(operation_data["operationAmount"]["amount"])
    else:
        from_convert = operation_data["operationAmount"]["currency"]["code"]
        amount = operation_data["operationAmount"]["amount"]
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={from_convert}&amount={amount}"
        headers = {"apikey": os.getenv("API_KEY_APILAYER")}
        response = requests.request("GET", url, headers=headers)
        return response.json()["result"]


# print(currency_conversion({
#     "id": 41428829,
#     "state": "EXECUTED",
#     "date": "2019-07-03T18:35:29.512364",
#     "operationAmount": {
#       "amount": "8221.37",
#       "currency": {
#         "name": "USD",
#         "code": "USD"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "MasterCard 7158300734726758",
#     "to": "Счет 35383033474447895560"
#   }))
