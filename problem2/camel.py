name = input("camelCase: ")
print("snakecase: ", end="") 
for letter in name:
    if letter.isupper():
        print("_" + letter, end="")
    else:
        print(letter, end="") 


