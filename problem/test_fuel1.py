import pytest
from fuel1 import convert, guage
def test_value_error():
    with pytest.raises(ValueError):
        convert("cat/dog")
def Zero_divission_error():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")
def test_convert():
    #assert convert("cat/dog") == ValueError 
    assert convert("1/4") == 25 

