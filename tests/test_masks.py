from src.masks import get_mask_card_number
from src.masks import get_mask_account
import pytest

@pytest.mark.parametrize('card_input, card_output',[('123456789123','1234 56** ****'),('123','Не корректные данные')])

def test_get_mask_card_number (card_input, card_output):
   assert get_mask_card_number(card_input) == card_output

@pytest.mark.parametrize('account_input, account_output',[('73654108430135874305','**4305'),('123456789123','Не корректные данные')])

def test_get_mask_account (account_input, account_output):
   assert get_mask_account(account_input) == account_output