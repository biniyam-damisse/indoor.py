import random 
while True: 
    try:     
        name = int(input("Level1: ")) 
        if name > 0:
            break 
    except:
        continue
k = random.randint(1, name)
while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess > k:
                print("Too large!")
            elif guess < k:
                print("Too small!")
            else:
                print("Just right!")
                break
    except:
        continue

    


       


