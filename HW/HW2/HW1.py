
#task 1 -----------------------------------------
print("task 1 -----------------------------------------")
print("Get the next day")
'''Get the next day '''
day = int(input('Enter Day ---> '))
month = int(input('Enter Month ---> '))
year = int(input('Enter Year ---> '))

def NextYear(day,month, year):
#Years checking
    oldDay = day
    oldMonth = month
    oldYear = year
    if (year % 400 == 0):# leap year
        leapYear = True
    elif (year % 4 == 0):# leap year
        leapYear = True
    elif (year % 100 == 0):# not leap year
        leapYear = False
    
    else:
        leapYear = False
        
#Month checking  
 
    if month in (1, 3, 5, 7, 8, 10, 12):
        monthLength = 31
    if month == 2:
        if leapYear:
            monthLength = 29
        else:
            monthLength = 28
    else:
        monthLength = 30
      
#Day checking          
    if day < monthLength:
        day += 1
    else:
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
       
    print(oldDay,'/',oldMonth,'/',oldYear, '=>', day,'/',month,'/',year)
    
#function calling   
NextYear(day,month, year)

#task 2 -----------------------------------------

print("task 2 -----------------------------------------")
print("Checking sum of special digit- even or odd")
'''Checking sum of special digit - even or odd'''
num = int(input('Enter number ---> '))
if num <0:
        num = num*(-1)
        
def Digits(num):
    
    count = 0
    temp = num
    while (num > 0):
        num = num//10
        count = count + 1
    #print ("Total number of digits : ",count)
#one digits    
    if count == 1:
        num %=2
        if num == 1:
            print('one digits - odd',end=" ")
        else:
            print('one digits - even',end=" ")
#two digits 
    if count ==2:
        firs = temp//10
        second=temp%10 
        if (firs+second)%2==1:
            print('two digits - odd',end=" ")
        else:
            print('two digits - even',end=" ")
#three digits
    if count == 3:
        first = temp//100
        second = (temp //10)%10
        third = temp%10 
        #print(first,second,third)
        
        if  (first+third)%2 == 1:
            print('three digits - odd',end=" ")
        else:
            print('three digits - even',end=" ")
#four digits       
    if count == 4:
        second = (temp//100)%10
        third = (temp //10)%10
        #print(second,third)
        if (second+third)%2==1:
            print('four digits - odd',end=" ")
        else:
            print('four digits - even',end=" ")
#five digits
    if count ==5:
        middle = (temp//100)%10
        #print(middle)
        if middle%2==1:
            print('five digits - odd',end=" ")
        else:
            print('five digits - even',end=" ")     
    print()   
#function calling 

print("Digits(",num,")"," => ",end=" ")                   
Digits(num) 



#task 3 -----------------------------------------

print("task 3 -----------------------------------------")
print("Checking number digits if all digits even or odd")
'''Checking number digits if all digits even or odd'''

num = int(input('Enter number ---> '))
if num <0:
        num = num*(-1)
def GoodOreder (num):
    count=0
    while (num>0):
        temp=num%2
        num//=10
        if temp==1:
            count =  count+1          
    if count>0:
        return False
    else:
        return True

#function calling 
print('GoodOreder(',num,')',' =>',GoodOreder (num))
    
#task 4 -----------------------------------------

print("task 4 -----------------------------------------")
print("Print triangle")
'''Print triangle'''
def alphapat(num):
    
    for i in range(1, num+1):
        for space in range (0,num-i):
            print(' ',end="")
        for j in range(0, i):
            if(j==0 or i==0):
                print(i,end="")
            elif (i==j+1):
                print(' ',i,end=" ")
            elif(i==num):
                
                for k in range(num-1,0,-1):
                    print(k,end='')
                    
                for k in range(2,num+1,+1):
                    print(k,end='')
                    flag=0
                if (flag ==0):
                    break
            else:
                print('  ',end="")
                
        print()
        
    
            
num = int(input("Enter number: ---> "))
if num <0:
        num = num*(-1)
if(num>9):
    print("Error! Illegal Number")
print("Figure(",num,")")
alphapat(num)




#task 5 -----------------------------------------
print("task 5 -----------------------------------------")
print("Sum big digit with amount of number digits")
'''Sum big digit with amount of number digits'''
def Value(num):

    def countDigit(num):
        return math.ceil(math.log(num, 10))

    def findMaxDigit(num):
        def Max(x,y):
            if (x>y): return x
            else: return y

        if (num==0):
            return 0
        else:
            a = num%10
            b = num//10
            if(a>b):
                return Max(num%10,findMaxDigit(num//10))
            else: return Max(num%10,findMaxDigit(num//10))
            
    return findMaxDigit(num)+countDigit(num)

        
   
import math      
num = int(input('Enter number ---> '))   
if num <0:
        num = num*(-1)
print("Value(",num,") => ", Value(num))

    

#task 6 -----------------------------------------
print("task 6 -----------------------------------------")
print("Find number in pascal triangle")
'''Find number in pascal triangle'''
def Pascal(r, c):
    if r<c:
        return -1
    if c == 0:
        return 1
    if r == 0:
        return c
    return (r * Pascal(r-1, c-1)) / c
    
  
r = int(input("Enter row: ---> "))
c = int(input("Enter column: ---> "))
    
#print(pascal(2,3))  
#print(pascal(10,4)) 
print("Pascal(",r,",",c,") => ", int(Pascal(r, c))) 

#task 7 -----------------------------------------

print("task 7 -----------------------------------------")
print("Reduce zero from number")
'''Reduce zero from number'''
def Reduce(num):
    if(num<0):
        num= num*(-1)
    if (abs(num)<10):
        return num
    elif(num%10==0):
        return Reduce(num//10)
    else:
        return Reduce(num//10)*10+num%10

num = int(input("Enter number: ---> "))
res = Reduce(num)
if(num<0):
    res=res*(-1)
print("Reduce(",num,")"," => ", res)

#task 8 -----------------------------------------

print("task 8 -----------------------------------------")
print("Check if number is prime")

'''Check if number is prime'''
def IsPrimary(num,a=2):
    
    if num <= 1:
        return True
    else:
        if a >= num:
            return True
        else:
            if num == 2: 
                return True
            elif (num % a) == 0:
                return False
            else:
                return IsPrimary(num,a+1)

    
    
    '''
    def IsPrim(x,k):
        if(k<=1):
            return True
        if(x%k==0):
            return False
        return IsPrim(x,k-1)
    return IsPrim(num,round(sqrt(num)))    
    '''

#from  math  import sqrt
num = int(input("Enter number: ---> "))  
print("IsPrimary(",num,")"," => ", IsPrimary(num))
