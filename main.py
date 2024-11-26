

def lists_rewers(primo: list[str | int]) -> list[str | int]:
    """Функция на полинромию"""
    new_spisok = []
    for i, v in enumerate(primo):
        if str(v) == str(v)[::-1]:
            new_spisok.append(v)
    return new_spisok


print(lists_rewers([121, '141', '123', 145]))
