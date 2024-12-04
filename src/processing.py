def filter_by_state (addres_list: list, state_value: str) -> list:
    """Функция фильтровки по ключю state"""
    new_addres_list = []
    for index_list, value_list in enumerate(addres_list):
        if value_list['state'] == state_value:
            new_addres_list.append(value_list)
    return new_addres_list


def sort_by_date (data_list:list, reverse_key:bool = True ) -> list:
    """Функция сортировки данных"""
    return sorted( data_list, key= lambda x: x['date'], reverse = reverse_key)

