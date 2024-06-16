import re 
def main():
    print(count(input("Text: ")))
def count(s):
    d = re.findall(r"\b\W*um\W*", s, re.IGNORECASE)
    return len(d) 

if __name__ == "__main__":
    main() 