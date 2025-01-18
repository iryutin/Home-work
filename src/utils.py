import codecs
import json
import logging

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("D:/my_project2/pythonProject1/logs/utils.log")
file_formater = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def data_operatinons_convert(path: str) -> list:
    """Перевод json в список словарей"""
    logging.info(f"Запущена функция перевода файла {path} в строку")
    try:
        with codecs.open(path, "r", "utf_8_sig") as operatinon_file:
            try:
                operatinon_data = list(json.load(operatinon_file))
            except json.JSONDecodeError:
                logging.error(f"Ошибка обработки файла {path}")
                return []
    except FileNotFoundError:
        logging.error(f"Файл не найден {path}")
        return []
    logging.debug("Прога отработала")
    return operatinon_data


# print(data_operatinons_convert('D:/my_project2/pythonProject1/data/operations.json'))
