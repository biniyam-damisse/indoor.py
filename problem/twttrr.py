def main():
    name = input('Input: ') 
    print("Output: ", end="") 
    print(shorten(name))

def shorten(word):
    a = ['a', 'e', 'i', 'o', 'u']
    for k in word:
        if not k.lower in a:
            return k

if __name__ == "__main__":
    main() 