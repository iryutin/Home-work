import codecs
import json
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_hader = logging.FileHandler(f"logs/{__name__}.log")
file_formater = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_hader.setFormatter(file_formater)
logger.addHandler(file_hader)


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
    logging.debug(f"Прога отработала")
    return operatinon_data
