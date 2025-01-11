import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("D:/my_project2/pythonProject1/logs/masks.log")
file_formater = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера карты"""
    logger.debug(f"Введен номер карты {card_number}")
    if card_number.isdigit() and len(card_number) == 12:
        logger.debug("Номер карты верен")
        return f"{card_number[0:4]} {card_number[4:6]}** ****"
    else:
        logger.error(f"Номер карты {card_number} не верен")
        return "Не корректные данные"


def get_mask_account(account: str) -> str:
    """Функция маскировки номера счёта"""
    logger.info(f"Введен номер счёта {account}")
    if account.isdigit() and len(account) == 20:
        logger.info("Номер счёта верен")
        return "**" + account[-4:]
    else:
        logger.error(f"Номер счёта {account} не верен")
        return "Не корректные данные"
