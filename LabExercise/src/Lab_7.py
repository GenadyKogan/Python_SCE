# ------------------------------------------------
# Conventional Interfaces
# ------------------------------------------------
# S1 - Sum of n elements of Fibonacci sequence
# ------------------------------------------------
'''
def fib(k): 
    """Compute the kth Fibonacci number.""" 
    prev, curr = 1, 0 # curr is the first Fibonacci number. 
    for _ in range(k - 1): 
        prev, curr = curr, prev + curr
    return curr
#--------------------------------------------------
def iseven(n): 
    return n % 2 == 0
'''
#--------------------------------------------------
#nums = (5, 6, -7, -8, 9)
#tuple(filter(iseven, nums)) # => (6, -8)
#sum(map(abs, nums)) # => 35
#sum(map(abs, tuple(filter(iseven, nums))))
'''
def sum_even_fibs(n): 
    """Sum the even members of the first n Fibonacci numbers.""" 
    return sum(filter(iseven, map(fib, range(1, n+1)))) 
'''
# ------------------------------------------------
# S2
# ------------------------------------------------
#print(tuple('Spaces between words'.split())) # => ('Spaces', 'between', 'words') 
# ------------------------------------------------
'''
def first(s):
    """Return first letter of string"""
    return s[0]
# ------------------------------------------------
def iscap(s):
    """Return True if first letter is Capital Letter"""
    return len(s) > 0 and s[0].isupper() 
# ------------------------------------------------
def acronym(name): 
    """Return a tuple of the letters that form the acronym for name.""" 
    return tuple(map(first, filter(iscap, name.split()))) 
'''
# ------------------------------------------------
# ------------------------------------------------
#acronym('Sami shamoon Collage of Engineering Department of Software Engineering') #->('S', 'C', 'E', 'D', 'S', 'E')
# ------------------------------------------------

# ------------------------------------------------
# Generator expressions
# <map expression> for <name> in <sequence expression> if <filter expression> 
# ------------------------------------------------
# ------------------------------------------------
'''
def sum_even_fibs1(n): 
    return sum(fib(k) for k in range(1, n+1) if fib(k) % 2 == 0)
# ------------------------------------------------
def sum_even_fibs2(n): 
    return sum(fib(k) for k in range(1, n+1) if iseven(fib(k)))
# ------------------------------------------------
def acronym1(name): 
    return tuple(w[0] for w in name.split() if iscap(w))
# ------------------------------------------------
def acronym2(name): 
    return tuple(first(w) for w in name.split() if iscap(w))
'''
# ------------------------------------------------
#sum_even_fibs1(20) # => 3382
#acronym1('Sami shamoon Collage of Engineering Department of Software Engineering') #->('S', 'C', 'E', 'D', 'S', 'E')
# ------------------------------------------------
# ------------------------------------------------
# Reduce
# ------------------------------------------------
from operator import mul
from operator import add
from functools import reduce 
#reduce(mul, (1, 2, 3, 4, 5))
# ------------------------------------------------
'''def product_even_fibs(n): 
    """Return the product of the first n even Fibonacci numbers, except 0."""
    return (reduce(add, filter(iseven, map(fib, range(2, n+1)))))
# ------------------------------------------------
#print(product_even_fibs(8)) # => 123476336640
# ------------------------------------------------
def reduce_even_fibs(n,f): 
    return reduce(f, filter(iseven, map(fib, range(2, n+1))))
# ------------------------------------------------
#reduce_even_fibs(20,lambda x,y:x*y) #mul => 123476336640
#reduce_even_fibs(20,lambda x,y:x+y) #sum => 3382
'''
# ------------------------------------------------
# task 1
'''
def accumulate(x,f,l):
    for y in l:
        x= f(x,y)
    return x
'''
# ------------------------------------------------   
#print(accumulate(0, add, (1, 2, 3, 4, 5)))
# => 15
#print(accumulate(1, lambda x,y:x*y, [1, 2, 3, 4, 5]))
# => 120
#print(accumulate(1, lambda x,y:4*x-y, (1, 2, 3, 4, 5)))
# => 571
#print(accumulate(1, lambda x,y:4*x-y, (1, 2, 3, 4, 5)))
# ------------------------------------------------     
'''
def mymap(f,l):
    x=list(l)
    for i in range(len(x)):
        x[i] = f(x[i])
    return x         
'''
# ------------------------------------------------
#print(tuple(map(lambda x: x*x, range(1, 5))))
# => (1, 4, 9, 16)
#print(tuple(mymap(lambda x: x*x, range(1, 5))))
# => (1, 4, 9, 16)
# ------------------------------------------------
'''
from math import sqrt
def iseven(x): 
    return x % 2 == 0
# ------------------------------------------------
def issquare(x):  
    return int(sqrt(x)) **2 == x 
# ------------------------------------------------
def orfilter(f1,f2):
    def filter_func(x):
        return f1(x) or f2(x)
    return filter_func
'''
# ------------------------------------------------
#print(list(filter(orfilter(iseven, issquare), range(20))))
'''
from math import sqrt
def average_passed_grade(grades):
    s=tuple(filter(lambda x: x>=56,
                   map(lambda x : 10*sqrt(x),
                       filter(lambda x: x!=199,
                              grades))))
    return reduce(add,s)/len(s)
print(average_passed_grade([23, 64, 199, 20, 77, 98, 100, 199]))
'''
# ------------------------------------------------
#                       Q6
# ------------------------------------------------
'''
#a
make_pairs=lambda el,lst:tuple(map(lambda x : (el,x ),lst))
print(make_pairs(5,(1,2,3)))

# b:  two solutions
c_prod = lambda lst1, lst2: tuple(map(lambda x:make_pairs(x,lst2),lst1))
c_prod = lambda lst1, lst2: tuple(make_pairs(x,lst2) for x in lst1)
print(c_prod((1,2),(3,4)))

#c : two solutions
flat_c_prod=lambda lst1,lst2:reduce(add,c_prod(lst1,lst2) ,())
flat_c_prod = lambda lst1, lst2: reduce(lambda x,y:x+y, c_prod(lst1, lst2), ())
print(flat_c_prod((1,2),(3,4)))

#d
cond_c_prod=lambda p,lst1,lst2:flat_c_prod(tuple(filter(p,lst1)),tuple(filter(p,lst2)))
print(cond_c_prod(lambda x :type(x)==int,(1,2,3.5),(3,'a',4)))
'''