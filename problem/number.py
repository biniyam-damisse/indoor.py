while True:
    try: 
        x = int(input("what is x? "))
        #print(f"x is {x}")
    except ValueError:
        print("x is not an integer")
    else:
        break
print(f"x is {x}")