def main():
    dollars = dollar_to_float(input("how much was the meal? "))
    percent = percent_to_float(input("what precentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollar_to_float(d):
    d = d.replace("$", '')
    return float(d) 

def percent_to_float(p):
    p = p.replace("%", "") 
    return float(p) / 100

main() 