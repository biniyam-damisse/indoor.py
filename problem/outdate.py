months = [
    "January","February","March","April","May","June","July",
    "August","September","October","November","December",    
]
while True:
    date = input("Date: ")
    try:
        m, d, Y = date.split("/")
        if (int(m) >= 1 and int(m) <= 12) and (int(d) >= 1 and int(d) <= 31):
            break  
    except:
        try:
            M, D, Y = date.split(" ")
            for i in range(len(months[i])):
                if M == months[i]:
                    m = i + 1 
            d = D.replace(",","")
            if (int(m) >= 1 and int(m) <= 12) and (int(d) >= 1 and int(d) <= 31):
                break  
        except:
            print()
            pass
print(f"{Y}-{int(m):02}-{int(d):02}")
