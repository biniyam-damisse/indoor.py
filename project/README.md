# *Title:* Gregorian to Ethiopian Calander converter and vise-versal 
#### **Video Demo**:

<https://myfinalprojectofcs50>


#### **Description:**
      - A fully functional calander converter from gregorian calander into Ethiopian calander or vise-versal


Gregorian Calander year, month and days counting systems is very vary to some specific countries. For example Ethiopian use their own Calander and is a bit different from the rest of the world. And this project converts, Gregorian Calander into Ethiopian Calander. Or from Ethiopian Calander into Gregorian Calander.  


Ethiopia is eight years behind the rest of the world. Which means now in Ethiopia the year is not 2024-04-29. it is 2016-08-21. Years and days are eight years behind the rest of the world. And in Ethiopia case, every month always ends with 30 days. There is no variations like the Gregorian one. Since all the months end with same numbers of days, there are 5 or 6 days left to fulfill a one full year. or 365 days depending on the leap year. So Ethiopian use those 5 or 6 days together as month 13

  The project has four different functions and each of them are listed as bellow.

      - main functions 
      - Gregorian_converter functions 
      - Thrteen_month functions
      - Ethiopian_converter functions
      - Thrtheen

#### *Main Functions:*
  It is a function that contians all the other functions. 
It first ask the user to enter number one or two to indentify into which to convert. Then after the insertion, it again ask to enter the proper format of the calander. if the program get the proper format of the year. first it split it into year, month and day. Then convert each of them into an integer because down of the other functions it will use to add or substract to this number. 
if the user enter unformal number or Calander the interpreter exit via sys exit with the message of Incorrect Format. 
~~~ python
def main():
    ask = input(f"Press 1 to conevert into Ethiopian press 2 to convert into Gregorian ") 
    if ask == "1" or ask == "one" or ask == "ONE":
        try:
            k = input("Insert Year in YYYY-MM-DD format: ") 
            y, m, d = k.split("-") 
            w = int(y)
            g = int(d) 
            j = int(m) 
            kn = Gregorian_converter(w, j, g) 
            pn = thrteen_month(w, j, g) 
            if kn:
                print(kn) 
            else:
                print(pn) 
            sys.exit()
        except ValueError:
           sys.exit("Incorrect Format")
~~~

#### *Gregorian_converter Functions:*
 After receving the Calander from the user, it converts each year, month and days into Ethiopian year, month and day. But to convert it, first there are differnt things to consider. 
 Among them, the leap year and the 13 month of Ethiopian Calander are the main one. This 13 month is not common every year. It varies to 5 or 6 days depending on the leap year. So first I put all the Ethiopian year, that has 6 days on the 13 months in list of argument called 'b'. So this b contaians all the year that ends with 6 days. For example 2003, 2007, 2011, 2015, 2019 etc are some examples of the Ethiopian year that ends with day 6 in the last month of the year.  

 ~~~ python
 def Gregorian_converter(a, j, knn):
    b = []
    for _ in range(3, 5000, 4):
        b.append(_)
    if (a in b and j == 1) or (a in b and j == 4) or (a in b and j == 5) or (a % 4 == 0 and j == 2) or (a % 4  == 0 and j == 4) or ( a % 4 == 0 and j == 5) or (a % 4 != 0 and j == 4) or (a % 4 != 0 and j == 5) or (a % 4 != 0 and j == 1):
        if j == 4 and knn > 30:
            return "Invalid calander" 
        if a % 4 == 0 and j == 2 and knn > 29:
           return "Invalid calander"
        if knn >= 1 and knn <= 8:                       
            return(f"{a-8}-{j + 3:02}-{knn + 22:02}") 
        elif knn >= 9 and knn <= 31:        
            return(f"{a-8}-{j + 4:02}-{knn - 8:02}")  
        else:
            return "Invalid calander"
    elif (a in b and j == 2) or (a in b and j == 6) or (a in b and j == 7) or (a % 4 == 0 and j == 6 or a % 4 == 0 and j == 7) or ( a % 4 != 0 and j == 6 or a % 4 != 0 and j == 7 or a % 4 != 0 and j == 2): 
        if j == 2 and knn > 28:
            return "Invalid calander"
        if j == 6 and knn > 30:
            return "Invalid calander"
        if knn >= 1 and knn <= 7:
            return(f"{a-8}-{j + 3:02}-{knn + 23:02}")
        elif knn >= 8 and knn <= 31: 
            return(f"{a-8}-{j + 4:02}-{knn - 7:02}" ) 
        else:
            return "Invalid calander"
    elif a in b and j == 3 or (a % 4 == 0 and j == 1 or a % 4 == 0 and j == 3) or (a % 4 != 0 and j == 3):
        if knn >= 1 and knn <= 9:
            return(f"{a-8}-{j + 3:02}-{knn + 21:02}")
        elif knn >= 10 and knn <= 31: 
            return(f"{a-8}-{j + 4:02}-{knn - 9:02}" ) 
        else:
            return "Invalid calander"
    elif a in b and j == 8 or (a % 4 == 0 and j == 8) or (a % 4 != 0 and j == 8):
        if knn >= 1 and knn <= 6:
            return(f"{a-8}-{j + 3:02}-{knn + 24:02}") 
        elif knn >= 7 and knn <= 31: 
            return(f"{a-8}-{j + 4:02}-{knn - 6:02}" ) 
        else:
            return "Invalid calander"
    elif a in b and j == 11 or  (a in b and j == 12) or (a % 4 == 0 and j == 10) or a % 4 != 0 and j == 10:
        if j == 11 and knn > 30:
         return "Invalid calander"
        if knn >= 1 and knn <= 10:
         return(f"{a-7}-{j - 9:02}-{knn + 20:02}")
        elif knn >= 11 and knn <= 31:
         return(f"{a-7}-{j - 8:02}-{knn - 10:02}" )
    elif a in b and j == 10:
        if knn >= 1 and knn <= 11:
            return(f"{a-7}-{j - 9:02}-{knn + 19:02}")
        elif knn >= 12 and knn <= 31:
            return(f"{a-7}-{j - 8:02}-{knn - 11:02}" )
    elif (a % 4 == 0 and j == 12 or a % 4 == 0 and j == 11) or a % 4 != 0 and j == 12 or a % 4 != 0 and j == 11:
        if j == 11 and knn > 30:
              return "Invalid calander"
        if knn >= 1 and knn <= 10:
            return(f"{a-7}-{j - 9:02}-{knn + 21:02}") 
        elif knn >= 11 and knn <= 31:
            return(f"{a-7}-{j - 8:02}-{knn - 9:02}" ) 
    else:
       return "Invalid calander"
 ~~~
 #### *Thrteen_month functions:*

 This function a function that is used to convert into the Ethiopian 13 month Calander. Always 13 will be when it is septemeber or on the 9 month of the Gregorian Calander. Therefore this function is used to convert into the last month of Ethiopian Calander.

#### *Ethiopian_converter functions:* 
This function convert Ethiopian year, month and days into the proper Gregorian year, month and days. by adding 8 or sometimes 7 year and monthes to itself to get the correct Gregorian Calander.
#### *Thrtheen:*
This function is also used to convert the thrteen month of Ethiopians into the right Gregorian Calander. 
  
### How the project works:

When the user run for the program, they are asked to insert number 1 (one) or 2 (two) to decide from which Calander into which they want to convert.

     - if the insertion is NUMBER 1 it means that it is going to convert from Gregorian Calander into Ethiopian Calanders 

     - if the insertion is number 2 it means that convert from Ethiopian Calander into Gregorian Calander.

So, after they insert number 1 or 2, they are asked to insert the year in yyyy-mm-dd format. And finally it convert the insertion year, month and days into the Calander, they want it.

### Notice:

    -  The user should only insert 1 or one or ONE or 2 or two or TWO when asked for the insertion. this helps the program to identify to which to convert otherwise the program return the message incorrect format.
    -  Incorrect insertion of years, months and days will return invalid Calander
    -  The year month and days should be inserted in the format of yyyy-mm-dd otherwise the program will return invalid Calander



 

