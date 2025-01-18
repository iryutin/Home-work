from unittest.mock import patch

import pandas as pd

from src.file_reader import transformation_csv, transformation_excel


@patch("pandas.read_csv")
def test_transformation_csv(mock_get):
    """Тест функции transformation_csv"""
    mock_get.return_value = pd.DataFrame({"Yes": [50, 21], "No": [131, 2]})
    assert transformation_csv("") == [{"Yes": 50, "No": 131}, {"Yes": 21, "No": 2}]


@patch("pandas.read_excel")
def test_transformation_exel(mock_get):
    """Тест функции transformation_csv"""
    mock_get.return_value = pd.DataFrame({"Yes": [50, 21], "No": [131, 2]})
    assert transformation_excel("") == [{"Yes": 50, "No": 131}, {"Yes": 21, "No": 2}]
    mock_get.asser_