import re 
def main():
    print(validate(input("Ipv4 Address: ")))
def validate(Ip):
    ip = re.search(r"^[0-9]?[0-9]?[0-9]\.[0-9]?[0-9]?[0-9]\.[0-9]?[0-9]?[0-9]\.[0-9]?[0-9]?[0-9]?$", Ip)
    if ip:
        n = Ip.split(".")
        for nub in n:
            if int(nub) < 0 or int(nub) > 255:
                return False
        return True
    else:
        False

if __name__ == "__main__":
    main() 