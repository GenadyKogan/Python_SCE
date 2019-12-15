
#===============================================#

                # task 1

#===============================================#

def make_power(x,y):
    def dispatch(i):
        if i==0:return x
        elif i==1:return y
    return dispatch
#===============================================#
def getitePower(p,i):return p(i)
#===============================================#
def base(x):return getitePower(x,0)
#===============================================#
def power(x):return getitePower(x,1)
#===============================================#
def print_power(x):
    if power(x)>0 and power(x)<1: return x
    if power(x)==0 or power(x)==1:print('{0}'.format(base(x)) )    
    if power(x)==2:print('{0}'.format(base(x)*base(x)) ) 
    #return '{0}{1}{2}'.format(base(x),(lambda x:'^' if x>=0 else '^')(power(x)),power(x))
    print('{0}{1}{2}'.format(base(x),'^',power(x)))  
#===============================================#
def improve_power(x):return make_power(returnBase(base(x)), amountOfPower(base(x))*power(x))
#===============================================#
import math
def power_function(decimal, integer):
    num=1
    if integer>0:
        for i in range(integer):
            num=num*decimal
    if integer<0:
        num=1.0 # force floating point division
        for i in range(-integer):
            num=num/decimal
    return num

#===============================================#
def amountOfPower(n) : 
    if (n==1):return 1
    # Try all numbers from 2 to sqrt(n) as base 
    for x in range(2,(int)(math.sqrt(n))+1): 
        y = 2
        p = (int)(power_function(x,y)) 
        # Keep increasing y while power 'p' is smaller 
        # than n.  
        while(p<=n and p>0):
            if(p==n):return y
            y=y + 1
            p=power_function(x,y) 
    return 1
#===============================================#
def returnBase(n) : 
    if (n==1):return True
    # Try all numbers from 2 to sqrt(n) as base 
    for x in range(2,(int)(math.sqrt(n))+1) : 
        y = 2
        p = (int)(power_function(x,y)) 
        # Keep increasing y while power 'p' is smaller 
        # than n.  
        while (p<=n and p>0):
            if (p==n): return x
            y=y+1
            p=power_function(x,y) 
    return 1

#===============================================#
def isPower(n) : 
    if (n==1)  : 
        return True
    # Try all numbers from 2 to sqrt(n) as base 
    for x in range(2,(int)(math.sqrt(n))+1) : 
        y = 2
        p = (int)(math.pow(x, y)) 
        # Keep increasing y while power 'p' is smaller 
        # than n.  
        while (p<=n and p>0) : 
            if (p==n) : 
                return True
            y = y + 1
            p = math.pow(x, y) 
    return False
#print(isPower(19683))
#===============================================#
def mul_power(x,y):
    a=power_function(base(x),power(x))
    b=power_function(base(y),power(y))
    res = a*b
    if res> 0 and res<1:
        return print_power(res)
    #return res
    return make_power(returnBase(res), amountOfPower(res))

#===============================================#
def div_power(x,y):
    a=power_function(base(x),power(x))
    b=power_function(base(y),power(y))
    if returnBase(a)==returnBase(b) and amountOfPower(a)<amountOfPower(b):
        return make_power(returnBase(a), amountOfPower(a)-amountOfPower(b))
    
    res=a/b
    #print("res-->",res)
    #if res>0 and res<1:
        #return print_power(res)
    return make_power(returnBase(res), amountOfPower(res))
#===============================================#

#x= make_power(4,5)

#print(x)
#print(base(x))
#print(power(x))
#print(print_power(x))
#print(print_power(improve_power(x)))
#y=make_power(9,2)
#print(print_power(improve_power(y))) 
#print(print_power(mul_power(y,x))) 
#print_power(mul_power(improve_power(y),make_power(3,5)))

#print(print_power(div_power(mul_power(make_power(2,3),make_power(2,8)), make_power(2,4))))
#print( print_power(div_power(mul_power(improve_power(make_power(8,1)), improve_power(make_power(256,1))),improve_power(make_power(16,1)))))
#print(print_power(make_power(12,1))) 
#print(print_power(make_power(12,0))) 

#===============================================#

                # task 2

#===============================================#

def make_tree(value,left,right):
    def dispatch(message):
        if message == 'value':return value
        elif message == 'left_node':return left
        elif message == 'right_node':return right
    return dispatch
#===============================================# 
def getitem_node(f,i):return f(i)
#===============================================# 
def right(node):return getitem_node(node, 'right_node')
#===============================================#
def left(node):return  getitem_node(node,'left_node')
#===============================================#
def value(node):return getitem_node(node, 'value')
    #return node("value")
#===============================================#
def print_tree(tree):
    if tree!=None:
        print_tree(left(tree))
        print(value(tree),end=" ")
        print_tree(right(tree))
#===============================================#
def count_value(tree,val):
    if tree==None:return 0
    if value(tree)==val:return 1+count_value(left(tree),val)+ count_value(right(tree),val)
    return 0+count_value(left(tree),val)+ count_value(right(tree),val)
#===============================================#
def tree_BST(tree):
  
    if tree==None:return True  
    elif left(tree) != None:return value(tree)>value(left(tree)) and tree_BST(left(tree))
    elif left(tree) != None:return value(tree)<value(right(tree)) and tree_BST(right(tree))
    return tree_BST(left(tree)) and tree_BST(right(tree))
#===============================================#
def  tree_depth(tree): 
    if tree==None:return -1
    else:         
        lDepth=tree_depth(left(tree))
        rDepth=tree_depth(right(tree))
        if(lDepth>rDepth):return lDepth+1
        else:return rDepth+1
#===============================================#      
def tree_balanced(tree):
    if tree==None:return True
    lh=tree_depth(left(tree))
    rh=tree_depth(right(tree))
    if (abs(lh - rh) <= 1) and tree_balanced(left(tree)) is True and tree_balanced(right(tree)) is True:return True
    return False
#===============================================#
    
tree1=make_tree(12,   make_tree(6,make_tree(8,None,None),None),     make_tree(7, make_tree(8,None,None), make_tree(15,None,None) ) )
tree2=make_tree(12,      make_tree(6,make_tree(3,make_tree(1,None,None),None), make_tree(8,make_tree(7,None,None),None)),     make_tree(15,None,make_tree(20,make_tree(17,None, None),None))) 
tree3=make_tree(12,make_tree(17,None,None),make_tree(8,None,None))
#print_tree(tree1)
#print_tree(tree3) 
#print(value(left(right(left((tree2)))))) 
#print(count_value(tree1,8))
#print(tree_BST(tree1))
#print(tree_depth(tree2))
print(tree_balanced(tree2))