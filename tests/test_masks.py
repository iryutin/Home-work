from src.masks import get_mask_card_number

def test_get_mask_card_number ():
   assert get_mask_card_number('123456789123') == '1234 56** ****'