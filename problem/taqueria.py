name = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 31.00,
    "Quesadilla": 8.50,
    "Supper Burrito": 8.50,
    "Supper Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}
Z = 0
while True:
    try:
        item = input("Item: ").title() 
        if item in name:
            Z += name[item]
            print("Total: $", end="") 
            print(f"{Z:.2f}")
    except EOFError:
        print() 
        break