def main():
    plate = input("plate: ")
    if is_valid(plate):
        print("valid")
    else:
        print("invalid")   
def is_valid(s):
    if 2 < len(s) > 6:
        return False
    if s[0].isalpha() == False or s[1].isalpha() ==  False:
        return False  
    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
           if s[i] == "0": 
                return False   
           else:
               break    
        i = i + 1
    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False
    for character in s:
        if character in ['.', ' ', '|', '?']:
            return False
    return True

if __name__ == "__main__":
    main()