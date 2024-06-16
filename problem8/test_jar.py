from jar import Jar 
def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jarrr = Jar(4)
    assert jarrr.capacity == 4
    
def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🌞"
    jar.deposit(11)
    assert str (jar) == "🌞🌞🌞🌞🌞🌞🌞🌞🌞🌞🌞🌞"

def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2
    jar.deposit(3)
    assert jar.size == 5
    jar.deposit(2)
    assert jar.size == 7

def test_withdraw():
    jar = Jar()
    jar.deposit(6)
    jar.withdraw(4)
    assert jar.size == 2
    jar.withdraw(2)
    assert jar.size == 0
    
