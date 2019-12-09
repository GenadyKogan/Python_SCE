from operator import getitem
from fractions import gcd
#def make_rat(n, d):
    #return (n, d)
#help(getitem)
def numer(x):return getitem(x, 0)
def denom(x):return getitem(x, 1)
def str_rat(x):return '{0}/{1}'.format(numer(x), denom(x))
def add_rat(x, y):
        nx, dx = numer(x), denom(x)
        ny, dy = numer(y), denom(y)
        return make_rat(nx * dy + ny * dx, dx * dy)
def mul_rat(x, y):return make_rat(numer(x) * numer(y), denom(x) * denom(y))
def eq_rat(x, y):return numer(x) * denom(y) == numer(y) * denom(x)
def make_rat(n, d):
        g = gcd(n, d)
        return (n//g, d//g)

half = make_rat(1, 2)
print(str_rat(half))
third = make_rat(1, 3)
print(str_rat(mul_rat(half, third)))
print(str_rat(add_rat(third, third)))
print(str_rat(add_rat(third, third)))