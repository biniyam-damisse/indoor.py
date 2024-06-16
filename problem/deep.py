name = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
if name.strip() == "42":
    print("Yes")
elif name.strip().lower() == "forty-two":
    print("yes") 
elif name.strip().lower() == "forty two":
    print("YES")
else:
    print("No") 