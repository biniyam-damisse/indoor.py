import requests
import sys 
if len(sys.argv) == 2:
    try:
        num = float(sys.argv[1])
        sys.exit
    except:
        print("command-line argument is not a number")
else:
    sys.exit("Missing command-line argument") 
try:
    web = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    webbs = web.json()
    pick = webbs["bpi"]["USD"]["rate_float"]
    result = pick * num 
    print(f"${result:,.4f}") 
except requests.RequestException:
    sys.exit()
