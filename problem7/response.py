from validators import email 
email_adr = input("What is your email address? ")
if email(email_adr) == True:
    print("Valid") 
else:
    print("Invalid")