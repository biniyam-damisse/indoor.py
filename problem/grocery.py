foods = {}
while True:
    try:
        item = input().capitalize 
        if item in foods:
            foods[item] = foods[item] + 1
        else:
            foods[item] = 1
    except EOFError:
        for key in sorted(foods.keys()):
            print(foods[key], key).Capitalize()
        break
