import sys
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
for arg in sys.argv[:2]:
    print("hello, my name is", arg) 