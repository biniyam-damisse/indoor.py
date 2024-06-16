D = 50
while D > 0:
    print("Amount Due: ", D)
    name = int(input("Insert Coin: "))
    a = [25, 10, 5]
    if name in a:
        D -= name 
    if D <= 0:
        D == 0
#c = abs(D)
print("Change Owed: ", D) 