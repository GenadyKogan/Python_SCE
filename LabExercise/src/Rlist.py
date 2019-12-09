# ------------------------------------------------
#           ADT rlist(tuple) - recursive list
# ------------------------------------------------

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
def len_rlist(s):
# Return the length of recursive list s.
    length = 0
    while s != empty_rlist:
        
        s, length = rest(s), length + 1
        
    return length
def getitem_rlist(l,i):
    while i>0:
       
        l,i=rest(l),i-1
        print("rest(l) ---> ",l)
    return first(l) 
      
# ------------------------------------------------
counts=make_rlist(1,make_rlist(2,make_rlist(3,make_rlist(4,None))))

#print(first(counts))
print(getitem_rlist(counts, 3))


# ------------------------------------------------
#           ADT rlist(dispatch) - recursive list
# ------------------------------------------------
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
def getitem_pair(s,i):
    return s(i)
# ------------------------------------------------
def first(s):
    return getitem_pair(s,0)
# ------------------------------------------------
def rest(s):
    return getitem_pair(s,1)
# ------------------------------------------------
def len_rlist(s):
# Return the length of recursive list s.
    length = 0
    while s != empty_rlist:
        s, length = rest(s), length + 1
    return length
       
# ------------------------------------------------
counts=make_rlist(1,make_rlist(2,make_rlist(3,make_rlist(4,None))))
print(len_rlist(counts))
'''