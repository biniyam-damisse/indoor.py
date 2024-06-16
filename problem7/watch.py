import re 
def main():
    print(parse(input("HTML: ")))
def parse(s):
    if chann := re.search(r"^<iframe src=\"https?://(www\.)?youtube\.com/embed/([a-z0-9]+)\"></iframe>$", s, re.IGNORECASE):
        return ("https://youtu.be/" + chann.group(2))

if __name__ == "__main__":
    main() 
