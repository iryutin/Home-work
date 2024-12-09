def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера карты"""
    return f'{card_number[0:4]} {card_number[4:6]}** ****'


def get_mask_account(account: str) -> str:
    """Функция  маскировки номера счёта"""
    return "**" + account[-5:-1]
