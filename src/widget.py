def mask_account_card(account_card_date: str) -> str:
    """Функция маскировки счёта или карты"""
    if "счет" in account_card_date.lower():
        return f"Счет **{account_card_date[-4:]}"
    else:
        return f"{account_card_date[:-12]} {account_card_date[-12:-10]}** **** {account_card_date[-4:]}"


def get_date(date: str) -> str:
    """Функция форматирования даты"""
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"
