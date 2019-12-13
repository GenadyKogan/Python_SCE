from math import sqrt
# ------------------------------------------------
#       Q1(ADT Complex Number - pair)
# ------------------------------------------------
'''
def make_complex(a,b):
    return (a,b)
# ------------------------------------------------
def real(c):
    return c[0]
# ------------------------------------------------
def imag(c):
    return c[1]
# ------------------------------------------------
def str_complex(c):
    return '({0}{1}{2}i)'.format(real(c),(lambda x:'+' if x>=0 else '')(imag(c)),imag(c)) 
# ------------------------------------------------
def add_complex(c1,c2):
    return make_complex(real(c1)+real(c2),imag(c1)+imag(c2))
# ------------------------------------------------
def abs_complex(c):
    return sqrt(real(c)**2+imag(c)**2)    

# ------------------------------------------------
#       Q1 Complex Number
# ------------------------------------------------
c=make_complex(2,3)
print(c)
print(real(c))
print(imag(c))
print(str_complex(c))
print(str_complex(add_complex(c,c)))
print(abs_complex(c))
'''

# ------------------------------------------------
#       Q2(ADT Complex Number - dispatch)
# ------------------------------------------------

def make_complex(a,b):
    def dispatch(x):
        if x==0:
            return a
        elif x==1:
            return b
    return dispatch
# ------------------------------------------------
def getitem_pair(p, i):
    return p(i)
# ------------------------------------------------
def real(c):
    return getitem_pair(c,0)
# ------------------------------------------------
def imag(c):
    return getitem_pair(c,1)
# ------------------------------------------------
def str_complex(c):
    return '({0}{1}{2}i)'.format(real(c),(lambda x:'+' if x>=0 else '')(imag(c)),imag(c)) 
# ------------------------------------------------
def add_complex(c1,c2):
    return make_complex(real(c1)+real(c2),imag(c1)+imag(c2))
# ------------------------------------------------
def abs_complex(c):
    return sqrt(real(c)**2+imag(c)**2)    
# ------------------------------------------------
c=make_complex(2,3)
#print("c -->",c(1))
#print(real(c))
#print(imag(c))
#print(str_complex(c))
#print(str_complex(add_complex(c,c)))
#print(abs_complex(c))
#print(str_complex(add_complex(c,c)))

# ------------------------------------------------
#       Q3(ADT rlist - tuple)
# ------------------------------------------------
'''
empty_rlist = None
# ------------------------------------------------
def make_rlist(first,rest):
# Make a recursive list from its first element and the rest.
    return (first,rest)
# ------------------------------------------------
def first(s):
#Return the first element of a recursive list s.
    return s[0]
# ------------------------------------------------
def rest(s):
#Return the rest of the elements of a recursive list s.
    return s[1]
# ------------------------------------------------
counts=make_rlist(1,make_rlist(2,make_rlist(3,make_rlist(4,empty_rlist))))
#print(counts)

# ------------------------------------------------
#       Q3(Reverse Recursive List)
# ------------------------------------------------


def printRlist(s):
    while s != empty_rlist:
        print( first(s), end=', ')
        s=rest(s)
    print()    
# ------------------------------------------------
def rlistReverse(s):
    new_s=empty_rlist
    while s != empty_rlist:
        new_s= make_rlist(first(s),new_s)
        
        s= rest(s)
    return new_s

# ------------------------------------------------
#print('Recursive List: ',end='')
#printRlist(counts)
#print('Reverse Recursive List: ',end='')
print(printRlist(rlistReverse(counts)))
'''
'''

# ------------------------------------------------
#       Q4(ADT rlist - dispatch)
# ------------------------------------------------
'''
'''
empty_rlist = None
# ------------------------------------------------
def make_rlist(first,rest):
    def dispatch(x):
        if x==0:
            return first
        elif x==1:
            return rest
    return dispatch
# ------------------------------------------------
def getitem_pair(p, i):
    return p(i)
# ------------------------------------------------
def first(s):
#Return the first element of a recursive list s.
    return getitem_pair(s,0)
# ------------------------------------------------
def rest(s):
#Return the rest of the elements of a recursive list s.
    return getitem_pair(s,1)
# ------------------------------------------------
counts=make_rlist(1,make_rlist(2,make_rlist(3,make_rlist(4,empty_rlist))))
'''
# ------------------------------------------------
#       Q4(Reverse Recursive List)
# ------------------------------------------------
'''
def printRlist(s):
    while s != empty_rlist:
        print( first(s), end=', ')
        s=rest(s)
    print()    
# ------------------------------------------------
def rlistReverse(s):
    new_s=empty_rlist
    while s != empty_rlist:
        new_s, s = make_rlist(first(s),new_s),rest(s)
    return new_s
'''
# ------------------------------------------------
#print('Recursive List: ',end='')
#printRlist(counts)
#print('Reverse Recursive List: ',end='')
#printRlist(rlistReverse(counts))

