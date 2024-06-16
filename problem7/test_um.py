from um import count 
def test_before():
    assert count("you are the one that always um lugh") == 1 
    assert count("yummy") == 0
    assert count("UM, hey how are you doing? ") == 1
