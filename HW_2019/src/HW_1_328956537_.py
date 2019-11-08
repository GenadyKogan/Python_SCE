
'''====================================================================='''
# task 1
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
    #rownum = (num//2)+1
   
    #i =0
    #j= num-1
    
    #colnum = num
    '''==================================='''
    #for row in range (rownum):
        #for col in range(colnum):
            # \
            #if row == col and row!=rownum-1 and col!=rownum-1:
                #print(chr(92),end = "")
            # *
            #elif row == col :
                #print("*",end = "")
            # |    
            #elif col == rownum - 1:
                #print(chr(124),end = "")
            # /
            #elif row ==i  and col == j:
               # print(chr(47),end = "")
                #i = i+1
                #j = j-1
            # -
            #elif row == rownum-1:
                #print("-", end="")
            
            #else: print(end = " ")
            
        #print()
     
    i=0
    j=num-1
    for row in range (num):
        for col in range (num):
            # /
            if row == i and col == j:
                if row == col:
                    print("*",end = "")
                
                else:print(chr(47),end= "")
                i+=1
                j-=1
            # \   
            elif row  == col:
                print(chr(92),end ="")
            # |
            elif col == (num//2):
                    print(chr(124),end = "")
            # -
            elif row == (num//2):
                print("-", end="")
            else:
                print(end=" ")
        print()
                   
   
    '''==================================='''
   
    '''  n= (n//2)+1
    k = 0
    for i in range(n - 1, -1, -1): 
  
        
        for j in range(n - 1, k, -1): 
            print(' ', end = '') 
  
        if n== 4 and i ==3 and j ==1  and k == 0:
            print("*", end='')
        else: print(chr(47), end = '') 
  
         
        for j in range(1, k * 2): 
            print(' ', end = '') 
        if i<n-1: 
            print(chr(92), end = '') 
        print() 
        k += 1'''
            

def Main():
    print("Enter positive and not even number: ")
    while True:
        num = int(input())
        if num < 0 or num %2 ==0:
            print("Wrong number.Enter positive and not even number: ")
            continue
        else:
            break
    
    PrintFigure(num)

Main()

    