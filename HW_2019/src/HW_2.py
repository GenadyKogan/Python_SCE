#task 4

def Make_iterator(fn):
    '''Make_iterator return foo function that 
    will work in the iterator.
    Returns the n-th element in a sequence.'''
    x=-1
    def foo(): 
        nonlocal x 
        fn(x)
        x+=1
        return  fn(x)
    return foo

#fn = lambda n:2*n
#iterator = Make_iterator(fn)

#for i in range(4):     
    #print("iterator",iterator())
  
#for i in range(2,4):     
   # print("iterator", iterator())
 
#it = Make_iterator(fn)
#for i in range(2):
   # print("it" ,it())
  
#for i in range(2,4):     
   # print("iterator",iterator())
'''========================================================='''
#task 5
# c
def isPrime(x):
    '''Function check if a given number is Prime number'''
    if x < 2:
        return False
    elif x == 2:
        return True  
    for n in range(2, x):
        if x % n ==0:
            return False
    return True
#print(isPrime(2))
'''========================================================='''
# d
'''Using High-Order Functions which uses other 
functions and a sequence of data.
listFilter([2,4,5,6,7,13], isPrime) output will be [2,5,7,13]
listFilterMulti([2,4,5,6,7,13], [isPrime, isFib]) output will be [2,5,13]'''
def isFib(number):
    '''Function check if a given number is Fibonacci number'''
    num1 = 1
    num2 = 1
    while True:
        if num2 <= number:
            if num2 == number:
                return True
            else:
                tempnum = num2
                num2 += num1
                num1 = tempnum
        else:
            return False
'''========================================================='''
#print(isFib(8))    
# a
def listFilter(list,f):
    '''Function returns a corrected list
    using some boolean function and sequence list type.'''   
    tempList =[]
    # this loop doesn't  work in listFilterMulti function
    #for _ in range(len(list)):
        #a = list.pop()
        #if f(a)==True:
            #tempList.append(a)
    #tempList.reverse()
    
    for i in range(len(list)):
        if f(list[i])==True:
            tempList.append(list[i])
    list = tempList.copy()
    return  list
'''========================================================='''
# b
def  listFilterMulti(list, fList):
    '''Function using sequence of numbers and a 
    sequence of functions and returns a revised list.'''
    tempList = []
    for i in fList:
        tempList.append(listFilter(list,i))
    #for x in tempList[0]:
        #for y in tempList[1]:
            #if x==y:
                #tempList2.append(x)
    tempList = [x for x in tempList[0] for y in tempList[1] if x==y]
    return tempList
            
#print(listFilterMulti([2,4,5,6,7,13], [isPrime,isFib]))
#print(listFilter([2,4,5,6,7,13],isPrime))
#print(listFilter([2,4,5,6,7,13],isFib))
'''========================================================='''
# task 6
from math import sqrt
def approx_eq(x, y, tolerance=1.0e-20):
        return abs(x - y) >= tolerance

    
def Fixed_point(f,init):
    '''A fixed point (sometimes shortened to fixpoint,
    also known as an invariant point) 
    of a function is an element of the function's domain that is
    mapped to itself by the function.
    Uusing the "iterative enhancement" method
    A function return a Sabbath point'''
    y,x=init,f(init)
    for _ in range(52):
        if approx_eq(x,y):
            if x>y:
                return
            y=f(y)
            x=f(y)
    return x


print(Fixed_point(lambda x: sqrt(x), 4))        
print(Fixed_point(lambda x: x**2, 4))
