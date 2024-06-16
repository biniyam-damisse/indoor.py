import sys 
if len(sys.argv) < 3: 
    print("Too few command line arguments")
    sys.exit()
if len(sys.argv) > 3:
    print("Too many command line arguments")
