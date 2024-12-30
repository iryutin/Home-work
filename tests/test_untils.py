from src.utils import data_operatinons_convert
import pytest

def test_data_operatinons_convert (capsys):
    data_operatinons_convert('')
    captured = capsys.readouterr()
    assert captured.out == "Файл не найден\n"
    assert data_operatinons_convert('') == []
    x = data_operatinons_convert('C:/Users/user/PycharmProjects/Home-work/data/operations.json')
    assert len(x) == 101