import logging

import pandas as pd

logger = logging.getLogger("file_reader")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("D:/my_project2/pythonProject1/logs/file_reader.log")
file_formater = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def transformation_csv(file_way: str) -> list[dict]:
    """Функция принимает путь к файлу csv и выдаёт список словарей"""
    try:
        df = pd.read_csv(file_way, sep=";")
    except FileNotFoundError:
        logging.error(f"Файл не найден {file_way}")
        return []
    else:
        data = df.to_dict(orient="records")
        for dict_data in data:
            amount, currency_name, currency_code = (
                dict_data.pop("amount"),
                dict_data.pop("currency_name"),
                dict_data.pop("currency_code"),
            )
            dict_data.update(
                {"operationAmount": {"amount": amount, "currency": {"name": currency_name, "code": currency_code}}}
            )
        return data


def transformation_excel(file_way: str) -> list[dict]:
    """Функция принимает путь к файлу exel и выдаёт список словарей"""
    try:
        df = pd.read_excel(file_way)
    except FileNotFoundError:
        logging.error(f"Файл не найден {file_way}")
        return []
    else:
        data = df.to_dict(orient="records")
        for dict_data in data:
            amount, currency_name, currency_code = (
                dict_data.pop("amount"),
                dict_data.pop("currency_name"),
                dict_data.pop("currency_code"),
            )
            dict_data.update(
                {"operationAmount": {"amount": amount, "currency": {"name": currency_name, "code": currency_code}}}
            )
        return data
