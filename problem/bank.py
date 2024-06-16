def main():
    n = input("Greeting: ")
    k = value(n)
    print(f"${k}") 
def value(greeting):
    if "hello" in greeting.lower().strip():
        return 0
    elif "h" == greeting[0].lower().strip():
        return 20
    else:
        return 100

if __name__ == "__main__":
    main() 

  
 