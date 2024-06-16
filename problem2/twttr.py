name = input("Input: ")
c = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
print("Output: ", end="")

for letter in name:
    if not letter in c:
        print(letter.lower(), end="")
