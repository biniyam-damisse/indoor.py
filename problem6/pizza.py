import sys 
from tabulate import tabulate
import csv
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if ".csv" not in sys.argv[1]:
    sys.exit("Not a CSV file") 
Data = []
try:
    with open(sys.argv[1], "r") as file:
        read = csv.reader(file)
        for i in read:
            Data.append(i)
except FileNotFoundError:
    sys.exit("File does not exists")
print(tabulate(Data[1:], headers=Data[0], tablefmt="grid"))

