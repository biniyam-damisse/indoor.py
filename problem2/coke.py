coin = [25, 10, 5]
c = 50 
while c > 0:
    print("Amount Due: ", c)
    name = int(input("Insert coin: "))
    if name in coin:
        c = (c - name)
    if c <= 0:
        c == 0
d = abs(c)
print("Change Owed: ", d) 