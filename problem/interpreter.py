name = input("Expression: ")
x, y, z = name.split(" ") 
X = float(x)
Z = float(z) 

if y == "+":
    value = X + Z
if y == "-":
    value = X - Z
if y == "*":
    value = X * Z
if y ==  "/":
    value = X / Z
print(f"{value:.1f}") 
