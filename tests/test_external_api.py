from unittest.mock import patch

import pytest

from src.external_api import currency_conversion


@patch("requests.request")
def test_currency_conversion(mock_recvest, conversion_data_out, conversion_data_in):
    """Тест функции currency_conversion"""
    mock_recvest.return_value.json.return_value = conversion_data_out
    assert currency_conversion(conversion_data_in) == 100.0
