def main():
    name = input("camelCase: ")
    n = snakecase(name)
def snakecase(n):
    #n = input("camelcase: ") 
    print("snakecase: ", end="") 
    for letter in n:
        if letter.isupper():
            print( "_" + letter.lower(), end="")
        else:
            print(letter, end="")
    #print()          
main()
