import codecs
import json


def data_operatinons_convert(path: str) -> list:
    """Перевод json в список словарей"""
    try:
        with codecs.open(path, "r", "utf_8_sig") as operatinon_file:
            try:
                operatinon_data = list(json.load(operatinon_file))
            except json.JSONDecodeError:
                print("Ошибка обработки файла")
                return []
    except FileNotFoundError:
        print("Файл не найден")
        return []
    return operatinon_data
