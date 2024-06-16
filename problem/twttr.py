name = input('Input: ')
a = ['a', 'e', 'i', 'o', 'u']
print("Output: ", end="")

for L in name:
    if not L.lower() in a:
        print(L , end="") 

