
#Task 4 --------------------------------------------------
print("Task 4 ------------------------------------------- Task 4")
'''
def Trapez_rule(f, a, b, n):
    h = float(b - a) / n
    s = 0.0
    s += f(a)/2.0
    print(f(a))
    for i in range(1, n):
        s += f(a + i*h)

    s += f(b)/2.0
    return s * h

print( Trapez_rule(lambda x:x**9, 0.0, 10.0, 10000))
'''

def Trapez_rule(f, a, b, n):
    h = (b-a)/float(n)
    s = 0.5*(f(a) + f(b))
    for i in range(1,n,1):
        s = s + f(a + i*h)
    return h*s

print( Trapez_rule(lambda x:x**9, 0.0, 10.0, 10000))
print()
'''
def Trapez_rule(f,a,b,n):

    
    delta =((b-a)/n)
    summ = (delta*(f(a)+f(b))/2) + delta*summation(a+delta,b-delta,f,lambda x:x+delta)
    return summ
    

def summation(a,b,f,step):
    total=0
    while a<=b:
        total+=f(a)
        a=step(a)
    return total


print(Trapez_rule(lambda x: x**9,0.0,10.0,100000))

'''
#Task 5 --------------------------------------------------
print("Task 5 ------------------------------------------- Task 5")
#C -  myPrime
def myPrime(x): 
    
    if x<2:
        return False
    if x==2:
        return True;
    else:
        for i in range(2,x):
            if x%i==0:
                return False
        return True   
#D - isFib
def isFib(x):
     
    a,b=0,1
    if x==a or x==b:
        return True
    c=a+b
    while(c<=x):
        if c==x:
            return True
        a=b
        b=c
        c=a+b
    return False    
#A - myFilter(l,func)    
def myFilter(l,func):
    for i in l:
        y = func(i)
        if (y == False):
            l.remove(i)
    return l        
#B - myFilterMulti(l,funcL)
def myFilterMulti(L,funcL): 
    for _ in range(len(L)):
        for i in L:
            y=funcL[1](i)
            x=funcL[0](i)
            if (x==False) or (y==False):
                L.remove(i)   
    if len(funcL)>2:
        newl=[]
        for i in L:
            temp=funcL[2]
            if  temp(i)==True:
                newl.append(i)                 
        L = newl  
    return L    

print("List ---> ",[2,4,5,6])
print("After function myFilter ---> ",myFilter([2,4,5,6],myPrime))
print()
print("List ---> ",[ 2,4,5,6,7,13])
print("After function myFilterMulti ---> ", myFilterMulti([ 2,4,5,6,7,13],[myPrime,isFib]))
print()
print("List ---> ",[2,4,5,13,41,55,53,107,144])
print("After function myFilterMulti ---> ", myFilterMulti ([2,4,5,13,41,53,89,107,144],[myPrime,isFib,lambda x: 9<x<100]))
print()
 
#Task 6 --------------------------------------------------
print("Task 6 ------------------------------------------- Task 6 ")

def square(x):
    return x**2
def incr(x):
    return x+1      


def repeat(f,num):
    if num==0:
        return (lambda x: x)
    return (lambda x: f (repeat(f, num-1)(x)))
        
print(repeat(incr,4)(2))
print(repeat(square,2)(5))


'''
def square(x):
    return x**2
def successor(x):
    return x+1      


def compose(f, g):
        def h(x):
            return f(g(x))
        return h

add_one_and_square = compose(square, successor)

print(add_one_and_square(5))
'''
'''
def square(x):
    return x**2

def incr(x):
    return x+1

def compose(f,g):
    return lambda x: f(g(x))
    
def repeated(f,reps):
 
    g=f
    for _ in range(1,reps):
        g = compose(f,g)
    return g


print(repeated(incr,4)(2))
print(repeated (square,2)(5))
'''

