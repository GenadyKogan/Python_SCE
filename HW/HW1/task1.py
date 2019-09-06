
# =========== Task 1 =========== #

def CheckDate(dd,mm,yyyy):
    """check year"""
    if yyyy<0:
        return False
    """check month"""
    if mm <1 or mm>12:
        return False
    """check days in the month"""
    if mm==1:
        if dd<1 or dd>31:
            return False
    if mm==2:
        if dd<1 or dd>28:
            return False
    if mm==3:
        if dd<1 or dd>31:
            return False 
    if mm== 4:
        if dd<1 or dd>30:
            return False
    if mm==5:
        if dd<1 or dd>31:
            return False         
    if mm==6:
        if dd<1 or dd>30:
            return False
    if mm==7:
        if dd<1 or dd>31:
            return False
    if mm==8:
        if dd<1 or dd>31:
            return False
    if mm==9:
        if dd<1 or dd>30:
            return False
    if mm==10:
        if dd<1 or dd>31:
            return False
    if mm==11:
        if dd<1 or dd>30:
            return False
    if mm==12:
        if dd<1 or dd>31:
            return False
    return True   

#print(CheckDate (5,10,1987)) 
#print(CheckDate (10,14,2017))    
#print(CheckDate (31,11,2018))

# =========== Task 2 =========== #

def RemoveMaxDigit(num):
    rev_num = 0
    chekcNum = 0
    max = 0
    temp = num
    temp2 = num
    """search max dig"""
    while temp2>0:
        chekcNum = temp%10
        if chekcNum>max:
            max = chekcNum
        temp = temp //10
        temp2=temp2//10
    #print(max)
    """revers number"""
    while num>0:
        res = num%10
        if res !=max:
            rev_num = rev_num*10+res
        num = num//10
    #print(rev_num)
    newNum = 0
    #print(rev_num)
    while rev_num>0:
        newNum = newNum*10+rev_num%10 
        rev_num = rev_num//10
    return newNum
    
#print(RemoveMaxDigit(3567267))  # ---> 35626         
#print(RemoveMaxDigit (3333) )   # ---> 0
   
# =========== Task 3 =========== #

def CalculateIntegral (n, x): 
    ans = 1
    k=1
    for i in range(0,n,1):
        #divider =(k*(2*i+1))
        """according to the formula"""
        x = ((-1)**i)*(x**(2*i+1))/(k*(2*i+1))
        k=k*i
        """if divide by zero"""
        if k==0:
            k=1
        ans = ans +x
    return ans
  
# Driver program to test above function 
#print(CalculateIntegral (2, 4))

"""for x in range (start, finish, step) star<finish"""
"""for x in range(star,finish,-step) start>finish"""

# =========== Task 4 =========== #

def AreAmicableNumbers(numA,numB):
    SumNumA =0
    SumNumB =0
    i=1
    """sum of numA"""
    while i <= numA-1 : 
        if (numA % i==0) : 
            SumNumA = SumNumA + i
        i = i + 1
    i=1
    """sum of numB"""    
    while i <= numB-1 : 
        if (numB % i==0) :  
            SumNumB = SumNumB + i
        i = i + 1     
    #print(SumNumA,SumNumB)
    """check sum of numbers: sum of numA with numB, sum of numB with numA"""
    if SumNumB == numA and SumNumA == numB:
        return True
    else: return False
    
#print(AreAmicableNumbers(284,220))

# =========== Task 5 =========== #

def CheckArithmeticSeries(num,d):
    if d==1:return False
    if num<10 :
        return True
    """divide numbers"""
    first = (int((num/10)%10))
    second = (int(num%10))
    #print('second',second)
    #print('first',first)
    """check difference between digits"""
    if second - first !=d:
        return False
    return CheckArithmeticSeries(num/10,d)
    
    
#print(CheckArithmeticSeries (3579,2))

# =========== Task 6 =========== #
def PrintX(num,space):
    """stop condition"""
    if(num<0):
        return False
    if(num>space):
        print_space(space)
        print("*",end='')
        print_space(num-2)
        print("*",end='')
        print_space(space)
        print()
        PrintX(num-2,space+1)
    if (num>1):
        print_space(space)
        print("*",end='')
        print_space(num-2)
        print("*",end='')
        print_space(space)
        print()
    else:
        print_space(space)
        print("*")
"""help function make space"""
def print_space(amount):
    if amount==1:
        print(' ',end='')
        return False
    elif amount <=0:
        return False
    print(' ',end='')
    print_space(amount-1)
    
"""Driver program to test above function """   
#PrintX(7,0)    
