

def Younger():
    nameA  = input("Enter a  name of the first person ")
    print("Enter a  birthdate of " + nameA)
    dayA = input("Day: ")
    monthA = input("Month: ")
    yearA  = input("Year: ")
    
    nameB  = input("Enter a  name of the second person ")
    print("Enter a  birthdate of " + nameB)
    dayB = input("Day: ")
    monthB = input("Month: ")
    yearB = input("Year: ")
    
    if yearA > yearB:print(nameA + " is younger")
    elif yearA < yearB:  print(nameB + " is younger")
    elif yearA == yearB:
        if monthA>monthB:print(nameA + " is younger")
        elif monthA < monthB:  print(nameB + " is younger") 
        elif monthA == monthB:
            if dayA>dayB:print(nameA + " is younger")
            elif dayA<dayB:print(nameB + " is younger")
            else:print(nameA +" and " + nameB + " are same age")
Younger()       