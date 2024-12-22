import pytest

from src.decorators import log

def test_log(capsys):
    @log()
    def callitka(x=True):
        if x != True:
            raise TypeError('TypeError')
        else:
            pass
    print(callitka())
    captured = capsys.readouterr()
    assert captured.out == 'callitka ok\nNone\n'
    print(callitka(False))
    captured = capsys.readouterr()
    assert captured.out == 'callitka error: TypeError. Inputs: (False,), {}\nNone\n'