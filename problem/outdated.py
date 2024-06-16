
months = [
    "January","February","March","April","May","June","July",
    "August","September","October","November","December",    
]
while True:
    dates = input("Date: ").title() 
    print("Date: ", end="")
    try:
            d, m, y = dates.split(" ") 
            if m in months:
                print(f"{m} {d}, {y}")   
    except ValueError:
        d, m, y = dates.split("/")
        if not m in months:
            print(f"{y}-0{d}-0{m}") 
    while True:
        dates == ValueError



