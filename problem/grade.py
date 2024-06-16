def main():
    ሰአት = input("what is the time? ")
    time = convert(ሰአት)
    if 7 <= time <= 8:
        print("breakfast time") 
    if 13 <= time <= 14:
        print("lunch time")
    if 18 <= time <= 19:
        print("dinner time")
  
    
def convert(t):
    hr, min = t.split(":")
    N_min = float(min) / 60 
    return float(hr) + N_min


if __name__ == "__main__":
    main()

