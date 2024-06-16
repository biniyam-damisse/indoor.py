import sys
from pyfiglet import Figlet
import random 
figlet = Figlet()

if len(sys.argv) == 1:
    israndom = True
elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
    israndom =False

else:
    sys.exit(1)

#you can then get a list of available fonts with code like this

figlet.getFonts()
msg = input("Input: ")
if israndom == False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print("Invalid usage")
        sys.exit(1)
else:
    font = random.choice(figlet.getFonts())

msg = input("Input: ")

print("Output:")
print(figlet.renderText(msg))