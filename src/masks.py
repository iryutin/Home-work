def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера карты"""
    if card_number.isdigit() == True and len(card_number) == 12:
        return f"{card_number[0:4]} {card_number[4:6]}** ****"
    else:
        return "Не корректные данные"


def get_mask_account(account: str) -> str:
    """Функция маскировки номера счёта"""
    if account.isdigit() == True and len(account) == 20:
        return "**" + account[-4:]
    else:
        return "Не корректные данные"
