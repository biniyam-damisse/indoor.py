import sys
def main():
    ask = input("Press 1 to conevert into Ethiopian press 2 to convert into Gregorian\n")
    if ask == "1" or ask == "one" or ask == "ONE":
        try:
            k = input("Insert Gregorian Year in YYYY-MM-DD format: ") 
            y, m, d = k.split("-") 
            w = int(y) 
            g = int(d) 
            j = int(m) 
            kn = Gregorian_converter(w, j, g) 
            pn = thrteen_month(w, j, g) 
            if kn:
                print(f"Ethiopian: {kn}") 
            else:
                print(f"Ethiopian: {pn}") 
            sys.exit()
        except ValueError:
           sys.exit("Incorrect Format") 
    elif ask == "2" or ask == "two" or ask == "TWO":
        try:
            k = input("Insert Ethiopian Year in YYYY-MM-DD format: ") 
            y, m, d = k.split("-") 
            w = int(y) 
            g = int(d) 
            j = int(m) 
            etk = Ethiopian_converter(w, j, g)
            thp = thrtheen(w, j, g) 
            if etk:
                print(f"Gregorian: {etk}") 
            else:
                print(f"Gregorian: {thp}") 
            sys.exit() 
        except ValueError:
           sys.exit("Incorrect Format")
    else:
        print("Invalid Press")    
def Gregorian_converter(a, j, knn):
    b = []
    for _ in range(3, 5000, 4):
        b.append(_) 
    if (a in b and j == 1) or (a in b and j == 4) or (a in b and j == 5) or (a % 4 == 0 and j == 2) or (a % 4  == 0 and j == 4) or ( a % 4 == 0 and j == 5) or (a % 4 != 0 and j == 4) or (a % 4 != 0 and j == 5) or (a % 4 != 0 and j == 1):
        if j == 4 and knn > 30:
            return "Invalid calander" 
        if a % 4 == 0 and j == 2 and knn > 29:
           return "Invalid calander"
        if knn >= 1 and knn <= 8:                       
            return(f"{a-8}-{j + 3:02}-{knn + 22:02}") 
        elif knn >= 9 and knn <= 31:        
            return(f"{a-8}-{j + 4:02}-{knn - 8:02}")  
        else:
            return "Invalid calander"
    elif (a in b and j == 2) or (a in b and j == 6) or (a in b and j == 7) or (a % 4 == 0 and j == 6 or a % 4 == 0 and j == 7) or ( a % 4 != 0 and j == 6 or a % 4 != 0 and j == 7 or a % 4 != 0 and j == 2): 
        if j == 2 and knn > 28:
            return "Invalid calander"
        if j == 6 and knn > 30:
            return "Invalid calander"
        if knn >= 1 and knn <= 7:
            return(f"{a-8}-{j + 3:02}-{knn + 23:02}")
        elif knn >= 8 and knn <= 31: 
            return(f"{a-8}-{j + 4:02}-{knn - 7:02}" ) 
        else:
            return "Invalid calander"
    elif a in b and j == 3 or (a % 4 == 0 and j == 1 or a % 4 == 0 and j == 3) or (a % 4 != 0 and j == 3):
        if knn >= 1 and knn <= 9:
            return(f"{a-8}-{j + 3:02}-{knn + 21:02}")
        elif knn >= 10 and knn <= 31: 
            return(f"{a-8}-{j + 4:02}-{knn - 9:02}" ) 
        else:
            return "Invalid calander"
    elif a in b and j == 8 or (a % 4 == 0 and j == 8) or (a % 4 != 0 and j == 8):
        if knn >= 1 and knn <= 6:
            return(f"{a-8}-{j + 3:02}-{knn + 24:02}") 
        elif knn >= 7 and knn <= 31: 
            return(f"{a-8}-{j + 4:02}-{knn - 6:02}" ) 
        else:
            return "Invalid calander"
    elif a in b and j == 11 or  (a in b and j == 12) or (a % 4 == 0 and j == 10) or a % 4 != 0 and j == 10:
        if j == 11 and knn > 30:
         return "Invalid calander"
        if knn >= 1 and knn <= 10:
         return(f"{a-7}-{j - 9:02}-{knn + 20:02}")
        elif knn >= 11 and knn <= 31:
         return(f"{a-7}-{j - 8:02}-{knn - 10:02}" )
    elif a in b and j == 10:
        if knn >= 1 and knn <= 11:
            return(f"{a-7}-{j - 9:02}-{knn + 19:02}")
        elif knn >= 12 and knn <= 31:
            return(f"{a-7}-{j - 8:02}-{knn - 11:02}" )
    elif (a % 4 == 0 and j == 12 or a % 4 == 0 and j == 11) or a % 4 != 0 and j == 12 or a % 4 != 0 and j == 11:
        if j == 11 and knn > 30:
              return "Invalid calander"
        if knn >= 1 and knn <= 10:
            return(f"{a-7}-{j - 9:02}-{knn + 21:02}") 
        elif knn >= 11 and knn <= 31:
            return(f"{a-7}-{j - 8:02}-{knn - 9:02}" ) 
    else:
       return "Invalid calander"
def thrteen_month(a, wr, k):
    b = []
    for _ in range(3, 5000, 4):
        b.append(_) 
    if a in b and wr == 9:                                                                       
        if k >= 1 and k <= 5:
            return f"{a-8}-{wr+3}-{k + 25}" 
        elif k >=6 and k <= 11:
            return f"{a-8}-{wr+4}-{k - 5:02}"
        elif k >= 12 and k <= 30:
            return f"{a-7}-{wr-8:02}-{k-11:02}"

    elif a not in b and wr == 9:
        if k >= 1 and k <= 5:
            return f"{a-8}-{wr+3}-{k + 25}" 
        elif k >=6 and k <= 10:
            return f"{a-8}-{wr+4}-{k - 5:02}"
        elif k >= 11 and k <= 30:
            return f"{a-7}-{wr-8:02}-{k-10:02}"
        else:
            return "Invalid calander"
def Ethiopian_converter(a, j, knn):
    b = []
    for _ in range(3, 5000, 4):
        b.append(_)
    if (a in b and j == 1) or (a not in b and j == 3): 
        if knn >= 1 and knn <= 20:           
         return(f"{a+7}-{j + 8:02}-{knn + 10:02}") 
        elif knn >= 21 and knn <= 30:        
         return(f"{a+7}-{j + 9:02}-{knn - 20:02}") 
        else:
         return "Invalid calander"

    elif a in b and j == 2:
        if knn >= 1 and knn <= 21:
          return(f"{a+7}-{j + 8:02}-{knn + 10:02}") 
        elif knn >= 22 and knn <= 30: 
          return(f"{a+7}-{j + 9:02}-{knn - 21:02}" ) 
        else:
          return "Invalid calander"

    elif a in b and j == 3:
        if knn >= 1 and knn <= 21:
         return(f"{a+7}-{j + 8:02}-{knn + 9:02}") 
        elif knn >= 22 and knn <= 30:  
         return(f"{a+7}-{j + 9:02}-{knn - 21:02}")  
        else:
         return "Invalid calander"

    elif a in b and j == 4:
        if knn >= 1 and knn <= 22:
         return(f"{a+7}-{j + 8:02}-{knn + 9:02}") 
        elif knn >= 23 and knn <= 30: 
         return(f"{a+8}-{j - 3:02}-{knn - 22:02}" ) 
        else:
         return "Invalid calander"

    elif a in b and j == 5 or a in b and j == 9 or ( a not in b and j == 9):
        if knn >= 1 and knn <= 23:
         return(f"{a+8}-{j - 4:02}-{knn + 8:02}")
        elif knn >= 24 and knn <= 30: 
         return(f"{a+8}-{j - 3:02}-{knn - 23:02}" ) 
        else:
         return "Invalid calander"

    elif a in b and j == 6:
        if knn >= 1 and knn <= 21:
         return(f"{a+8}-{j - 4:02}-{knn + 7:02}")
        elif knn >= 22 and knn <= 30: 
         return(f"{a+8}-{j - 3:02}-{knn - 21:02}" ) 
        else:
         return "Invalid calander"
    elif a in b and j == 7 or (a not in b and j == 5) or (a not in b and j ==7):
        if knn >= 1 and knn <= 22:
         return(f"{a+8}-{j - 4:02}-{knn + 9:02}")
        elif knn >= 23 and knn <= 30: 
         return(f"{a+8}-{j - 3:02}-{knn - 22:02}" ) 
        else:
         return "Invalid calander"

    elif a in b and j == 8 or ( a not in b and j == 8):
        if knn >= 1 and knn <= 22:
         return(f"{a+8}-{j - 4:02}-{knn + 8:02}")
        elif knn >= 23 and knn <= 30: 
         return(f"{a+8}-{j - 3:02}-{knn - 22:02}" ) 
        else:
         return "Invalid calander"

    elif a in b and j == 10 or (a not in b and j == 10): 
        if knn >= 1 and knn <= 23:
         return(f"{a+8}-{j - 4:02}-{knn + 7:02}")
        elif knn >= 24 and knn <= 30: 
         return(f"{a+8}-{j - 3:02}-{knn - 23:02}" ) 
        else:
         return "Invalid calander"

    elif a in b and j == 11 or ( a not in b and j == 11):
        if knn >= 1 and knn <= 24:
         return(f"{a+8}-{j - 4:02}-{knn + 7:02}") 
        elif knn >= 25 and knn <= 30: 
         return(f"{a+8}-{j - 3:02}-{knn - 24:02}" ) 
        else:
         return "Invalid calander"

    elif a in b and j == 12 or (a not in b and j == 12):
        if knn >= 1 and knn <= 25:
         return(f"{a+8}-{j - 4:02}-{knn + 6:02}") 
        elif knn >= 26 and knn <= 30: 
         return(f"{a+8}-{j - 3:02}-{knn - 25:02}" ) 
        else:
         return "Invalid calander"
    elif a not in b and j == 1:
        if knn >= 1 and knn <= 19:
         return(f"{a+7}-{j + 8:02}-{knn + 11:02}") 
        elif knn >= 20 and knn <= 30: 
         return(f"{a+7}-{j + 9:02}-{knn - 19:02}" ) 
        else:
         return "Invalid calander"
    elif a not in b and j == 2:
        if knn >= 1 and knn <= 20:
         return(f"{a+7}-{j + 8:02}-{knn + 11:02}") 
        elif knn >= 21 and knn <= 30: 
         return(f"{a+7}-{j + 9:02}-{knn - 20:02}" ) 
        else:
         return "Invalid calander"
    elif a not in b and j == 4:
        if knn >= 1 and knn <= 21:
         return(f"{a+7}-{j + 8:02}-{knn + 10:02}") 
        elif knn >= 22 and knn <= 30: 
         return(f"{a+8}-{j - 3:02}-{knn - 21:02}" ) 
        else:
         return "Invalid calander"
    elif a not in b and j == 6:
        if knn >= 1 and knn <= 21:
         return(f"{a+8}-{j - 4:02}-{knn + 8:02}") 
        elif knn >= 22 and knn <= 30: 
         return(f"{a+8}-{j - 3:02}-{knn - 21:02}" ) 
        else:
         return "Invalid calander"
    elif a not in b and j == 12:
        if knn >= 1 and knn <= 25:
         return(f"{a+8}-{j - 4:02}-{knn + 6:02}") 
        elif knn >= 26 and knn <= 30: 
         return(f"{a+8}-{j - 3:02}-{knn - 25:02}" ) 
        else:
         return "Invalid calander"
    else:
       return "Invalid calander" 
def thrtheen(a, j, knn):
    b = []
    for _ in range(3, 5000, 4):
        b.append(_)
    if a in b and j == 13 or a not in b and j == 13:
        if a not in b and j == 13 and knn > 5:
           return "Invalid calander"
        elif knn >= 1 and knn <= 6:
            return(f"{a+8}-{j - 4:02}-{knn + 5:02}")
        else:
            return "Invalid calander"        
    else:
        return "Invalid calander" 
if __name__== "__main__":
    main() 
