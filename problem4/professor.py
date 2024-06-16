import random
def main():
    der = get_level()
    result = tryeir(der)
    print("result: ", result)

def get_level():
    while True:
        try:
            der1 = int(input("Level: "))
            if der1 == 1 or der1 == 2 or der1 == 3:
                break
        except:
            pass
    return der1
def generate_integer(der1):
    if der1 == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif der1 == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x , y
def mukera(x, y):
    i = 1
    while True <=3:
        try:
            M = int(input(f"{x} + {y} = "))
            if M == (x + y):
                return True
            else:
                i += 1
                print("EEE")
        except:
            i += 1
            print("EEE")
    print(f"{x} + {y} = {x+y}")
    return False
def tryeir(der1):
    i = 1
    result = 0
    while i <= 10:
        x , y = generate_integer(der1)
        mels = mukera(x, y)
        if mels == True:
            result += 1
        i += 1
    return result

if __name__ == "__main__":
    main()