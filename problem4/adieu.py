import inflect
n = []
s = "adieu"
while True:
    try:
        who= input("Name: ").title()
        n.append(who)      
    except KeyboardInterrupt:
        print()
        break
x = inflect.engine()
k = x.join(who) 
print(f"{s,s}, to", {k})
