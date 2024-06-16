from bank import value
def test_value1():
    assert value("hello") == 0
    assert value("what up man hello") == 0
    assert value("HelLO") == 0
    assert value("HELLO") == 0
def test_value2():
    assert value("h") == 20
    assert value("H") == 20
    assert value("hey you are you okay? ")
def test_value3():
    assert value(" i love cs50 ")
    assert value("you know me?") == 100 
    assert value("YOU KNOW WHAT I LOVE YOU")