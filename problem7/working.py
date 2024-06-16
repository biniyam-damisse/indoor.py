import re 
def main():
    print(convert(input("Hours: ")))

def convert(s):
    # (0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)
    if MATCH := re.search(r"^(([0-9](?:[0-2])?):?([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])* ([A-P]M))$", s):
        return ( MATCH.groups())
#if MATCH := re.search(r"^(([0-9](?:[0-2])?):?([0-5](?:[0-9])?)? AM(?:PM)? to (([0-9](?:[0-2])?):?([0-5](?:[0-9])?)? AM(?:PM)?)) $", s):


if __name__ == "__main__":
    main() 