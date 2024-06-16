while True:
    name = input("Fraction: ")
    try:
        x, y = name.split("/")
        X = int(x)
        Y = int(y)
        Z = X / Y
        #f = int()
        if Z <= 1:
            break
    except (ValueError, ZeroDivisionError):
        pass 
z = Z * 100
if 1 >= z:
    print("E")
elif 99 <= z: 
    print("F")
else:
    print(f"{z:.0f}%")
       
    


 