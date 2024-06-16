def main():
    name = input("Fraction: ")
    percentage = convert(name)
    M = guage(percentage)
    print(M)
def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/") 
            a = int(x)
            b = int(y) 
            Z = a / b 
            if Z <= 1:
                return int(Z * 100)
            else:
                pass
        except (ValueError, ZeroDivisionError):
            raise         
def guage(K): 
    if 1 >= K:
        return("E") 
    elif 99 <= K: 
        return("F")
    else:
        return(f"{str(K)}%") 
        
if __name__ == "__main__":
    main()