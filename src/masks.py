def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера карты"""
    mask_card_number = []
    i = 0
    while i <= 12:
        if i == 4:
            mask_card_number.append(card_number[i : i + 2] + "**")
        elif i == 8:
            mask_card_number.append("****")
        else:
            mask_card_number.append(card_number[i : i + 4])
        i += 4
    return " ".join(mask_card_number)


def get_mask_account(account: str) -> str:
    """Функция  маскировки номера счёта"""
    return "**" + account[-5:-1]
