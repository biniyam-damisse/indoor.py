name = input("camelCase: ")
print("snake_case: ", end="")
for subject in name:
    if subject.isupper():
        print("_" + subject.lower(), end="", sep="")
    else:
        print(subject, end="") 
        print()