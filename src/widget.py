import datetime


def mask_account_card(account_card_date: str) -> str:
    """Функция маскировки счёта или карты"""
    cards_names = ["maestro", "mastercard", "visa classic", "visa platinum", "visa gold"]
    if account_card_date == "":
        return ""
    if "счет" in str(account_card_date).lower():
        return f"Счет **{account_card_date[-4:]}"
    else:
        for card_name in cards_names:
            if card_name in str(account_card_date).lower():
                return f"{account_card_date[:-12]} {account_card_date[-12:-10]}** **** {account_card_date[-4:]}"
        return "Не корректные данные"


def get_date(date: str) -> str:
    """Функция форматирования даты"""
    date_time_obj = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    new_date = str(date_time_obj.date())
    return ".".join(reversed(new_date.split("-")))
