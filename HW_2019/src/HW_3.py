from test.test_tools.test_unparse import nonlocal_ex


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
    
#tree1=make_tree(12,   make_tree(6,make_tree(8,None,None),None),     make_tree(7, make_tree(8,None,None), make_tree(15,None,None) ) )
#tree2=make_tree(12,      make_tree(6,make_tree(3,make_tree(1,None,None),None), make_tree(8,make_tree(7,None,None),None)),     make_tree(15,None,make_tree(20,make_tree(17,None, None),None))) 
#tree3=make_tree(12,make_tree(17,None,None),make_tree(8,None,None))
#print_tree(tree1)
#print_tree(tree3) 
#print(value(left(right(left((tree2)))))) 
#print(count_value(tree1,8))
#print(tree_BST(tree1))
#print(tree_depth(tree2))
#print(tree_balanced(tree2))

#===============================================#

                # task 3

#===============================================#
from functools import reduce
def get_prices(nameOfStore,products,sales):
    #res3=list(map(lambda x:x[1],list(filter(lambda x:x[0]==nameOfStore,sales ))))
    #return tuple(map(lambda x: (x[0],x[1]-x[1]*res3[0]), products))
    return tuple(map(lambda x: (x[0],x[1]-x[1]*list(map(lambda x:x[1],list(filter(lambda x:x[0]==nameOfStore,sales ))))[0]), products))
#===============================================#
def get_prices_dict(nameOfStore,products,sales):
    return dict(zip(products.keys(), list(map(lambda x: x-x*sales[nameOfStore], products.values()))))
    
    
#===============================================#

# ----------------------------version of ViktorTheGreat--------------------------------------------------------
sales_gimel = {'s1':{'t1':0.2, 't2':0.1}, 's2':{'t1':0.1, 't2':0.2},'s3':{'t1':0.3, 't2':0.5}}
types = {'t1':('p2', 'p4'), 't2':('p1', 'p3')}
def get_prices_by_type(shopName,prod_dict,sales_gimel,types):
    #the types of discount in the given shop
    discountTypes = sales_gimel[shopName]
    #lets create a calculationTuple:(discount,products_tuple) 
    calculationTuple = tuple(map(lambda x:(discountTypes[x],types[x]) if x in discountTypes else print('Wrong data'),types))
    #use the calculation tuple to apply each discount to the proper type
    result = dict(map(lambda x:(x,prod_dict[x]-prod_dict[x]*calculationTuple[0][0]) if x in calculationTuple[0][1] else
                      (x,prod_dict[x]-prod_dict[x]*calculationTuple[1][0]) ,prod_dict))
    return result
# -------------------------------------------------------------------------------------------------------------
#print(get_prices_by_type('s1', prod_dict, sales_gimel, types))
# -------------------------------------------------------------------------------------------------------------
#def get_prices_by_type(nameOfStore,prod_dict,sale_dict,types):
    #print("prod_dict-->",prod_dict)
    #print(sales[nameOfStore])
    #res=sales[nameOfStore]
    
    #return res
    #return tuple(map(lambda x: (x[0],x[1]-x[1]*list(map(lambda x:x[1],list(filter(lambda x:x[0]==nameOfStore,sales ))))[0]), products))

products = (('p1',1000),('p2',2000),('p3',5000),('p4',100)) 
#sales = (('s1',0.2),('s2',0.3),('s3',0.1))
#print(get_prices_dict('s1', products, sales)) 
prod_dict = dict(products) 
#sale_dict = dict(sales)
sales = {'s1':{'t1':0.2, 't2':0.1}, 's2':{'t1':0.1, 't2':0.2},'s3':{'t1':0.3, 't2':0.5}}
types = {'t1':('p2', 'p4'), 't2':('p1', 'p3')}  
#print(get_prices_dict('s1', prod_dict, sale_dict))
#print(get_prices_by_type('s1', prod_dict, sales, types))

#===============================================#

                # task 4

#===============================================#
def coding():
    newKey={}
    key={'reverse_word':None,'reverse_string':None}
    alphabet={'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j', 'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't', 'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z'}
    def set_key(step):
        
        nonlocal newKey   
        if type(step)==tuple:
            dic_len = len(alphabet)
            # Reduce the shift to the dic length
            #shift = shift % dic_len
            # convert the dict to a tupple to reference by index
            list_dic = [(k,v) for k, v in alphabet.items()]
            # Create the new shifted dict
            shifted = {
                list_dic[x][0]: list_dic[ (x + step[0]) % dic_len ][1] for x in range(dic_len) }
            if step[1]=='yes': newKey['reverse_word']=True
            if step[1]=='no': newKey['reverse_word'] =False
            if step[2]=='yes': newKey['reverse_string']=True
            if step[2]=='no': newKey['reverse_string'] =False
            newKey.update(newKey)
            newKey.update(shifted)
            return 'done'
        else: newKey=step
    def encoding(sentence):
        'replacing letters'
        encoding_dict ={k: v for k, v in newKey.items() if k not in key}
        sentence = ''.join([encoding_dict.get(i, i) for i in sentence])
        
        
        # need to change
        #----------------------------------------------------#
        sentence=' '.join(word[::-1] for word in sentence.split(" ")) 
        sentence=' '.join(reversed(sentence.split(' ')))
        #print("encoding-->",sentence)
        #----------------------------------------------------#
        return sentence
    def decoding(sentence):
        keydec=dispatch('export_key')
        if keydec=='key empty':return 'key empty' 
        else:
            
            # need to change
            #----------------------------------------------------#
            sentence=' '.join(reversed(sentence.split(' ')))
            sentence=' '.join(word[::-1] for word in sentence.split(" ")) 
            #----------------------------------------------------#

            decoding_dict2 = dict((y,x) for x,y in keydec.items())
            sentence = ''.join([decoding_dict2.get(i, i) for i in sentence])
            return sentence
    def empty_key():
        keydec=dispatch('export_key')
        keydec= {}
        #newKey={k: v for k, v in key.items() if k not in keydec.items()}
        newKey=keydec
        dispatch('set_key',newKey)
        return 'done'
    def export_key():
        if newKey=={}:return 'key empty'
        else: return newKey
    def import_key(sendKey):
        if sendKey=={}:return 'key empty'
        #elif 'export_key'!={}: return 'have a key'
        else: dispatch('set_key',sendKey)
        return 'done'
        
    def dispatch(message,args=None):
        if message=='set_key':return set_key(args)
        if message=='encoding':return encoding(args)
        if message=='empty_key':return empty_key()
        if message=='import_key':return import_key(args)
        if message=='export_key':return export_key()
        if message=='decoding':return decoding(args)
    return dispatch


code1=coding() 
code1('set_key',(-3,'yes','yes')) 
key=code1('export_key')
#print(key)
cstr=code1('encoding','the london is the capital of great britain') 
print(cstr)
dstr=code1('decoding',cstr) 
#print(dstr)
code2=coding()
dstr=code2('decoding','cstr')
#print(dstr)  
code2('import_key',key)
dstr=code2('decoding',cstr)
print(dstr)
code2('empty_key')
code2('export_key')
#===============================================#

                # task 5

#===============================================#
def parking(payForHour,numRegPla,numPriorPla,numVIPPla):
    listOfParking=[]
#===============================================#
    def print_list():
        i = len(listOfParking)-1
        def end():
            if i>0:
                return False
            else:
                return True
        def next():
            nonlocal i
            for item in listOfParking:
                print('{0}{1}{2}{3}{4}{5}'.format('car: ', item[0]  ,', parking type: ', item[1], ', parking time: ', item[2]))
                i=i-1
        return {"end":end,'next':next}
#===============================================#
    def print_parking(key):
        for item in listOfParking:    
            if item[1]==key:
                print('{0}{1}{2}{3}'.format('car: ', item[0], ', parking time: ', item[2]))
#===============================================#
    def next_time():
        for item in listOfParking:
            item[2]+=1   
#===============================================#
    def start_parking(key,value):
        nonlocal numRegPla
        nonlocal numPriorPla
        nonlocal numVIPPla
        if value=='Regular':numRegPla-=1
        if value=='Priority':numPriorPla-=1
        if value=='VIP':numVIPPla-=1
        for item in listOfParking:    
            if item[0]==key:
                item[1]=value
                item[2]=0
                return
        if numRegPla<=-1:return print('{0}{1}'.format('Regular ' ,'parking is full')) 
        if numPriorPla<=-1:return print('{0}{1}'.format('Priority ' ,'parking is full') )
        if numVIPPla<=0: return print('{0}{1}'.format('VIP ' ,'parking is full'))
        listOfParking.append([key, value,0])
#===============================================#
    def end_parking(numOfCar):
        nonlocal listOfParking
        paying=0
        for item in listOfParking:
            if item[0]==numOfCar: 
                paying = item[2]*payForHour
                print('{0}{1}{2}{3}{4}{5}{6}{7}'.format('car: ', item[0]  ,', parking type: ', item[1], ', parking time: ', item[2], ', payment: ', paying))
                listOfParking = [i for i in listOfParking if i[0] != numOfCar]
                
                return 
            
    return {'print_list':print_list, 'print_parking':print_parking, 'next_time':next_time,'start_parking':start_parking,'end_parking':end_parking}

#park1=parking(10,3,3,3) 

#park1['start_parking'](222,'Regular') 
#park1['start_parking'](223,'Regular') 
#park1['start_parking'](224,'Regular') 
#prn=park1['print_list']()
#while not prn['end'](): 
    #prn['next']()
#park1['next_time']()
#park1['end_parking'](224)
#prn=park1['print_list']() 
#park1['print_parking']('Regular')


def make_account():
    balance = 0
    def dispatch(x):
        if x == 'get':
            return balance
        elif x == 'change':
            def change(y):
                nonlocal balance
                if  dispatch('get') >= -y:
                    balance += y
                else:
                    return 'Out of funds during change'
                return balance
            return change
        elif x == 'move':
            def move(y,z):
                if z < 0:
                    return 'Negative transaction amount'
                elif dispatch('get') < z:
                    return 'Out of funds during change'
                else:
                    return (dispatch('change')(-z),y('change')(z))
            return move
        return balance
    return dispatch
# ------------------------------------------------
#a1 = make_account()
#a1 # => <function make_account.<locals>.dispatch at 0x0000022ABD3332F0>
#a2=make_account()
#a1('change')(20) # => 20
#print(a1('get')) # => 20
#a2('change')(50) # => 'Out of funds during change'
#print(a2("get"))
#a1('move')(a2, 7) # => (13, 7)
#a2('move')(a1, 2) # => (5, 15)
#a1('move')2, 30) # => 'Out of funds during change'
#a1('move')(a2, -30) # => 'Negative transaction amount'




