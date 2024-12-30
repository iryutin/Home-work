import os
from dotenv import load_dotenv
import requests

def currency_conversion(operations_data:list[dict]):
    for operation_data in operations_data:
        if operation_data['operationAmount']['currency']['code'] == 'RUB':
            return operation_data['operationAmount']['amount']
        else:
            from_convert = operation_data['operationAmount']['currency']['code']
            amount = operation_data['operationAmount']['amount']
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={from_convert}&amount={amount}"
            headers = {"apikey": os.getenv('API_KEY_APILAYER')}
            try:
                response = requests.request("GET", url, headers=headers)
            except requests.exceptions.ConnectionError:
                print("Connection Error. Please check your network connection.")
                return ''
            else:
                return response["result"]