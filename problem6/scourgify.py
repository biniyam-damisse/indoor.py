import sys 
import csv
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
    sys.exit("Not a CSV file") 
data = []
try:
    with open(sys.argv[1], "r") as file:
        r = csv.DictReader(file) 
        for i in r:
            name = i["name"].split(",")
            data.append({"first": name[1].lstrip(), "last":name[0], "house":i["house"]})       
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
with open(sys.argv[2], "w") as file:
    w = csv.DictWriter(file, fieldnames=["first", "last", "house"])
    w.writerow({"first":"first", "last":"last", "house":"house"})
    for i in data:
        w.writerow({"first": i["first"], "last": i["last"], "house": i["house"]})