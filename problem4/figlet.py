import sys
from pyfiglet import Figlet
from random import choice


figlet = Figlet() 

if len(sys.argv) < 2:
    name = input("Input: ")
    #figlet.setFont(font=f)
    cali = choice(figlet.getFonts())
    print("Output:")
    print(figlet.renderText(name))
elif len(sys.argv) > 2 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in figlet.getFonts():
    font = sys.argv[2]
    name = input("Input: ")
    figlet.setFont(font=sys.argv[2])
    cali = choice(figlet.getFonts())
    print("Output:")
    print(figlet.renderText(name))
else:
    sys.exit("Invalid usage")


