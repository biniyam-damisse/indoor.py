import re 
def main():
    print(convert(input("Hours: ")))

def convert(s):
    # (0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)
    if MATCH := re.search(r"^(([0-9](?:[0-2])?):?([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])* ([A-P]M))$", s):
        new = MATCH.groups()
        if int(new[1]) > 12 or int(new[5]) > 12:
            raise ValueError
        Tim = Nmatch(new[1], new[2], new[3])
        NTim = Nmatch(new[5], new[6], new[7])
        return f"{Tim} to {NTim}"
    else:
        raise ValueError 
def Nmatch(hr, min, ampm):
    if ampm == "PM":
        if int(hr) == 12:
            nhr = 12
        if int(hr) >= 1 and int(hr) < 12:
            nhr = int(hr) + 12
    else:
        if int(hr) == 12:
            nhr = 0
        else:
            nhr = int(hr)
    if min == None:
        nmin = ":00"
        NF = f"{nhr: 02}" + nmin
    else:
        NF = f"{nhr:02}" + ":" + min 
    return NF
if __name__ == "__main__":
    main() 