import sys 
from PIL import Image, ImageOps 
from os.path import splitext

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
m = splitext(sys.argv[1])
n = splitext(sys.argv[2]) 
if not m[1] in [".jpg", ".jpng", ".png"]:
    sys.exit("Invalid input")
if not n[1] in [".jpg", ".jpng", ".png"]:
    sys.exit("Invalid output")
if m[1].lower() != n[1].lower():
    sys.exit("Input and have different extensions")
try:
    im = Image.open(sys.argv[1]) 
except FileNotFoundError:
    sys.exit("Input does not exit")
shirtfile = Image.open("shirt.png")
size = shirtfile.size 
mup = ImageOps.fit(im, size) 
mup.paste(shirtfile, shirtfile)
mup.save(sys.argv[2])