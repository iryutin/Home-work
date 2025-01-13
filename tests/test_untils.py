from src.utils import data_operatinons_convert


def test_data_operatinons_convert(capsys):
    data_operatinons_convert("")
    captured = capsys.readouterr()
    assert captured.out == ""
    assert data_operatinons_convert("") == []
    x = data_operatinons_convert("D:/my_project2/pythonProject1/data/operations.json")
    assert len(x) == 101
