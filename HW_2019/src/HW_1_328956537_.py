'''====================================================================='''
# task 1
from _ast import Num

def Younger():
    nameA  = input('Enter a  name of the first person ')
    print('Enter a  birthdate of ' + nameA)
    dayA = input('Day: ')
    monthA = input('Month: ')
    yearA  = input('Year: ')
    
    nameB  = input('Enter a  name of the second person ')
    print('Enter a  birthdate of ' + nameB)
    dayB = input('Day: ')
    monthB = input('Month: ')
    yearB = input('Year: ')
    
    if yearA > yearB:print(nameA + ' is younger')
    elif yearA < yearB:  print(nameB + ' is younger')
    elif yearA == yearB:
        if monthA>monthB:print(nameA + ' is younger')
        elif monthA < monthB:  print(nameB + ' is younger') 
        elif monthA == monthB:
            if dayA>dayB:print(nameA + ' is younger')
            elif dayA<dayB:print(nameB + ' is younger')
            else:print(nameA +' and ' + nameB + ' are same age')
#Younger()
'''====================================================================='''
# task 2
def ReverseNumber(num):
    reverse = 0
    while num!=0:
        reverse = reverse * 10;
        reverse = reverse + num%10;
        num = num//10;
    return reverse

#print(ReverseNumber(13254))
'''=====================================================================''' 
# task 3      
def SortedDigits(num):
    digit,previous = 0,0
    while num>0:
        digit = num%10
        if previous != 0 and (digit > previous or digit == 0): return False 
        previous = digit
        num//= 10;
    return True
#print(SortedDigits (46789 ))
#print(SortedDigits (46719))
'''====================================================================='''

# task 4

def PrintFigure(num):
    """
    chr(47) = /
    chr(92) = \
    chr(124) = |
    """
    i=0
    j=num-1
    for row in range (num):
        for col in range (num):
            # /
            if row == i and col == j:
                if row == col:
                    print('*',end = '')
                
                else:print(chr(47),end= '')
                i+=1
                j-=1
            # \   
            elif row  == col:
                print(chr(92),end ='')
            # |
            elif col == (num//2):
                    print(chr(124),end = '')
            # -
            elif row == (num//2):
                print('-', end='')
            else:
                print(end=' ')
        print()
                   

def Main():
    print('Enter positive and not even number: ')
    while True:
        num = int(input())
        if num < 0 or num %2 ==0:
            print('Wrong number.Enter positive and not even number: ')
            continue
        else:
            break
    
    PrintFigure(num)

#Main()
'''=====================================================================''' 

# task 5

def Factorial(num):
    '''Function to calculate the factorial of any'''
    f = 1;
    while(num!=0):
        f=f*num
        num -=1
    return f

def SumOfFactorials(num):
    '''Function check if number = sum of factorials digits'''
    sum =0
    temp = num
    while(temp!=0):
        '''Calculate factorial of last digit'''
        sum = sum + Factorial(temp%10)
        '''Replace value of temp by temp / 10''' 
        temp = temp // 10;
    
    return (sum == num)


def Test():
    print('Enter positive integer number for range: ')
    while True:
        num = int(input())
        if num < 0:
            print('Wrong number.Enter integer number for range: ')
            continue
        else:
            break
    for x in range (num+1):
        if SumOfFactorials(x):
            print(x)
   
#Test()
'''=====================================================================''' 

# task 6

def RecPrint(begin, end, skip):
    if begin == end:
        print(begin)
        return begin
    
    if begin<end:
        print(begin)
        begin = begin + skip
        
        return RecPrint(begin, end, skip)
    

RecPrint(53,102,10)