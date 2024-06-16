from datetime import date
import sys
import re 
import inflect 
p = inflect.engine()
def main():
    BY = input("Date of Birth: ") 
    k = birth(BY) 
    print(k) 
def birth(s):
    name = re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", s)
    if name:
        y, m, d = s.split("-")      
    else:
        sys.exit("Invalid Date") 
    BD = date(int(y), int(m), int(d)) 
    DT = date.today()  
    M = (DT - BD).days * 1440
    result = p.number_to_words(M, andword="") 
    return f"{result.capitalize()} minutes" 
if __name__ == "__main__":
    main()    