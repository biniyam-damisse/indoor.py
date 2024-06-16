from project import Gregorian_converter, thrteen_month, Ethiopian_converter,thrtheen

def test_gregorian():
    assert Gregorian_converter(2024,4,28) == "2016-08-20"
    assert Gregorian_converter(2024,2,30) == "Invalid calander"
    assert Gregorian_converter(2023,2,29) == "Invalid calander"

def test_thrteen():
    assert thrteen_month(2024,9,6) == "2016-13-01"
    assert thrteen_month(2023,9,11) == "2015-13-06"
    assert thrteen_month(2023,9,12) == "2016-01-01"
    assert thrteen_month(2024,9,11) == "2017-01-01"
    assert thrteen_month(2024,9,10) == "2016-13-05"
def test_Ethiopian():
    assert Ethiopian_converter(2016,8,21) == "2024-04-29"
    assert Ethiopian_converter(2015,1,1) == "2022-09-11"
def test_mthrtheen():
    assert thrtheen(2016,13,1) == "2024-09-06"
    assert thrtheen(2016,13,6) == "Invalid calander"