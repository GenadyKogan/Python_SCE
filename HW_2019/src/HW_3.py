


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
'''function that return base of number'''
def base(x):return getitePower(x,0)
#===============================================#
'''function that return power of number'''
def power(x):return getitePower(x,1)
#===============================================#
def print_power(x):
    '''function: print number'''
    if power(x)>0 and power(x)<1:print(x)
    elif power(x)==0:print(1)
    elif power(x)==1:print('{0}'.format(base(x)) )    
   
    #return '{0}{1}{2}'.format(base(x),(lambda x:'^' if x>=0 else '^')(power(x)),power(x))
    else:print('{0}{1}{2}'.format(base(x),'^',power(x)))  
#===============================================#
'''improving number usung 2 function : returnBase and amountOfPower'''
def improve_power(x):return make_power(returnBase(base(x)), amountOfPower(base(x))*power(x))
#===============================================#

def power_function(decimal, integer):
    '''like power function'''
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
def sqrtt(x):
    '''like sqrt function'''
    n = 1
    for _ in range(10):
        n = (n + x/n) * 0.5
    return n
def amountOfPower(n) : 
   
    if (n==1):return 1
    # Try all numbers from 2 to sqrt(n) as base 
    for x in range(2,(int)(sqrtt(n))+1): 
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
    for x in range(2,(int)(sqrtt(n))+1) : 
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
def mul_power(x,y):
    '''mul two number'''
    a=power_function(base(x),power(x))
    b=power_function(base(y),power(y))
    res = a*b
    if res> 0 and res<1:
        return print_power(res)
    #return res
    return make_power(returnBase(res), amountOfPower(res))

#===============================================#
def div_power(x,y):
    '''div to number'''
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
#print_power(x)
#print_power(improve_power(x))
#print_power(mul_power(improve_power(x),make_power(2,5))) 
#y=make_power(9,2)
#print_power(improve_power(y)) 
#print_power(mul_power(x,y))
#print_power(mul_power(improve_power(y),make_power(3,5)))
#print_power(div_power(improve_power(y),make_power(3,5)))
#print_power(div_power(mul_power(make_power(2,3),make_power(2,8)), make_power(2,4)))
#print_power(div_power(mul_power(improve_power(make_power(8,1)), improve_power(make_power(256,1))),improve_power(make_power(16,1))))
#print_power(make_power(12,1))
#print_power(make_power(12,0))    

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
    '''function gets value as a parameter and returns how many times it appears in the tree'''
    if tree==None:return 0
    if value(tree)==val:return 1+count_value(left(tree),val)+ count_value(right(tree),val)
    return 0+count_value(left(tree),val)+ count_value(right(tree),val)
#===============================================#
def tree_BST(tree):
    '''function return True if tree is BST'''
    if tree==None:return True  
    elif left(tree) != None:return value(tree)>value(left(tree)) and tree_BST(left(tree))
    elif left(tree) != None:return value(tree)<value(right(tree)) and tree_BST(right(tree))
    return tree_BST(left(tree)) and tree_BST(right(tree))
#===============================================#
def  tree_depth(tree):
    '''function returns tree height'''
    if tree==None:return -1
    else:         
        lDepth=tree_depth(left(tree))
        rDepth=tree_depth(right(tree))
        if(lDepth>rDepth):return lDepth+1
        else:return rDepth+1
#===============================================#      
def tree_balanced(tree):
    '''function return true if a tree is a balanced tree '''
    if tree==None:return True
    lh=tree_depth(left(tree))
    rh=tree_depth(right(tree))
    if (abs(lh - rh) <= 1) and tree_balanced(left(tree)) is True and tree_balanced(right(tree)) is True:return True
    return False
#===============================================#
    
#tree1=make_tree(12,make_tree(6,make_tree(8,None,None),None),make_tree(7,make_tree(8,None,None),make_tree(15,None,None)))
#tree2=make_tree(12,make_tree(6,make_tree(3,make_tree(1,None,None),None),make_tree(8,make_tree(7,None,None),None)),make_tree(15,None,make_tree(20,make_tree(17,None, None),None)))
#print(tree1)
#print(tree2)
#print(value(tree1))   
#print(value(left(tree1)))
#print(value(right(left(tree2))))
#print_tree(tree1) 
#print()
#print_tree(tree2)
#print()
#print(count_value(tree1,8))
#print(tree_BST(tree1))
#print(tree_BST(tree2))
#print(tree_depth(tree1))
#print(tree_depth(tree2))
#print(tree_balanced(tree1))
#print(tree_balanced(tree2))
#===============================================#

                # task 3

#===============================================#
from functools import reduce
def get_prices(nameOfStore,products,sales):
    '''(('p1', 800.0), ('p2', 1600.0), ('p3', 4000.0), ('p4', 80.0)) '''
    #res3=list(map(lambda x:x[1],list(filter(lambda x:x[0]==nameOfStore,sales ))))
    #return tuple(map(lambda x: (x[0],x[1]-x[1]*res3[0]), products))
    return tuple(map(lambda x: (x[0],x[1]-x[1]*list(map(lambda x:x[1],list(filter(lambda x:x[0]==nameOfStore,sales ))))[0]), products))
products = (('p1',1000),('p2',2000),('p3',5000),('p4',100)) 
sales = (('s1',0.2),('s2',0.3),('s3',0.1))
#print(get_prices('s1', products, sales))
#===============================================#
def get_prices_dict(nameOfStore,prod_dict,sale_dict):
    ''' using dictionary
    {'p1': 800.0, 'p2': 1600.0, 'p3': 4000.0, 'p4': 80.0} '''
    return dict(zip(prod_dict.keys(), map(lambda x: x-x*sale_dict[nameOfStore], prod_dict.values())))
prod_dict = dict(products)     
sale_dict = dict(sales)
#print(get_prices_dict('s1', prod_dict, sale_dict))  
#===============================================#

sales = {'s1':{'t1':0.2, 't2':0.1}, 's2':{'t1':0.1, 't2':0.2},'s3':{'t1':0.3, 't2':0.5}} 
types = {'t1':('p2', 'p4'), 't2':('p1', 'p3')} 
def get_prices_by_type(nameOfStore,prod_dict,sales,types):
    '''step1: from sales ---> {'t1': 0.2, 't2': 0.1}
        step2: find in types key from step1 and replace ---> ((0.2, ('p2', 'p4')), (0.1, ('p1', 'p3')))
        step3: get answer ---> {'p1': 900.0, 'p2': 1600.0, 'p3': 4500.0, 'p4': 80.0'''
    return dict(map(lambda x:(x,prod_dict[x]- tuple(map(lambda x:(sales[nameOfStore][x],types[x]) if x in sales[nameOfStore] else False,types))[0][0]*prod_dict[x]) 
                    if x in tuple(map(lambda x:(sales[nameOfStore][x],types[x]) if x in sales[nameOfStore] else False,types))[0][1] else
                    (x,prod_dict[x]-tuple(map(lambda x:(sales[nameOfStore][x],types[x]) if x in sales[nameOfStore] else False,types))[1][0]*prod_dict[x])
                     ,prod_dict))
    #return {a: (b - sales.get(nameOfStore).get(tuple(filter(lambda x: True if a in types[x] else False, types))[0]) * b) for
            #a, b in prod_dict.items()}
#print(get_prices_by_type('s1', prod_dict, sales, types))
import operator
def accumulate_prices(nameOfStore, prod_dict, sales, types, func):
    '''using get_prices_by_type function with choosing values'''
    return reduce(func,get_prices_by_type(nameOfStore,prod_dict,sales,types).values()) 
#print(accumulate_prices('s1', prod_dict, sales, types, operator.add))
#===============================================#

                # task 4

#===============================================#
def coding():
    '''encrypting and decode the text that consists of words with one space'''
    key={'reverse_word':None,'reverse_string':None}
    newKey={}
    alphabet={'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j', 'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't', 'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z'}
    def set_key(step):
        '''Create an encryption key'''
        nonlocal newKey
        dic_len = len(alphabet)
        list_dic = [(k, v) for k, v in alphabet.items()]
        shifted = {
            list_dic[x][0]: list_dic[(x + step[0]) % dic_len][1]
            for x in range(dic_len)
        }
        if step[1] == 'yes': newKey['reverse_word'] = True
        else:key['reverse_word'] = False
        if step[2]=='yes': newKey['reverse_string']=True
        else: key['reverse_string'] =False
        newKey.update(newKey)
        newKey.update(shifted)
        return 'done'

    def encoding(sentence):
        '''encryption'''
        encoding_dict ={k: v for k, v in newKey.items() if k not in key}
        sentence = ''.join([encoding_dict.get(i, i) for i in sentence])
        sentence = sentence[::-1]
        return sentence


    def decoding(sentence):
        '''Decoding of sentence'''
        if bool(newKey)==True:
            encoding_dict = {k: v for k, v in newKey.items() if k not in key}
            decoding_dict2 = dict((y, x) for x, y in encoding_dict.items())
            sentence = ''.join([decoding_dict2.get(i, i) for i in sentence])
            sentence = sentence[::-1]
            return sentence
        elif bool(newKey)==False:
            return 'key empty'

    def import_key(sendKey):
        '''Encryption key import'''
        nonlocal newKey
        newKey=sendKey
        sendKey['reverse_string'] = True
        return 'done'

    def empty_key():
        '''returning to default key'''
        nonlocal newKey
        newKey={k: v for k, v in key.items() if k not in newKey.items()}
        return 'done'

    def export_key():
        '''Encryption key export'''
        if newKey['reverse_string']==True:return newKey
        else:return 'key empty'

    def dispatch(message,args=None):
        if message=='set_key':return set_key(args)
        if message=='encoding':return encoding(args)
        if message == 'decoding': return decoding(args)
        if message=='empty_key':return empty_key()
        if message=='export_key':return export_key()
        if message=='import_key':return import_key(args)
    return dispatch
#code1 = coding()
#print(code1('set_key', (-3, 'yes', 'yes')))
#key=code1('export_key')
#print(key)
#cstr = code1('encoding', 'the london is the capital of great britain')
#print(cstr)
#dstr=code1('decoding',cstr)
#print(dstr)
#code2=coding()
#dstr=code2('decoding',cstr)
#print(dstr)
#print(code2('import_key',key))
#dstr=code2('decoding',cstr)
#print(dstr)
#print(code2('empty_key'))
#print( code2('export_key'))

#===============================================#

                # task 5

#===============================================#
def parking(payForHour,numRegPla,numPriorPla,numVIPPla):
    listOfParking=[]
    
#===============================================#
    def print_list():
        '''function print details of each vehicle'''
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
        '''function print details of each vehicle that in the parking lot'''
        for item in listOfParking:    
            if item[1]==key:
                print('{0}{1}{2}{3}'.format('car: ', item[0], ', parking time: ', item[2]))
#===============================================#
    def next_time():
        '''promote hours of parking'''
        for item in listOfParking:
            item[2]+=1   
#===============================================#
    def start_parking(key,value):
        
        '''start parking'''
        nonlocal numRegPla
        nonlocal numPriorPla
        nonlocal numVIPPla
        if value=='Regular':numRegPla-=1
        if value=='Priority':numPriorPla-=1
        if value=='VIP':numVIPPla-=1
        if numRegPla<=-1 and value=='Regular':return print('{0}{1}'.format('Regular ' ,'parking is full')) 
        elif numPriorPla<=-1 and value=='Priority':return print('{0}{1}'.format('Priority ' ,'parking is full') )
        elif numVIPPla<=-1and value=='VIP': return print('{0}{1}'.format('VIP ' ,'parking is full'))
        listOfParking.append([key, value,1])
        
#===============================================#
    def end_parking(numOfCar):
        '''end parking'''
        nonlocal listOfParking
        flag=0
        paying=0
        for item in listOfParking:
            if item[0]==numOfCar: 
                paying = item[2]*payForHour
                print('{0}{1}{2}{3}{4}{5}{6}{7}'.format('car: ', item[0]  ,', parking type: ', item[1], ', parking time: ', item[2], ', payment: ', paying))
                listOfParking = [i for i in listOfParking if i[0] != numOfCar]
                flag=1
                break
        if flag==0: print("car not found") 
            
    return {'print_list':print_list, 'print_parking':print_parking, 'next_time':next_time,'start_parking':start_parking,'end_parking':end_parking}

park1=parking(10,3,3,3) 
#print( park1 )
park1['start_parking'](222,'Regular') 
#park1['start_parking'](223,'Regular') 
#park1['next_time']() 
#park1['start_parking'](224,'Regular') 
#park1['start_parking'](225,'Regular')
#park1['start_parking'](225,'VIP') 
#prn=park1['print_list']()
#print(prn)
#while not prn['end']():  
    #prn['next']() 
#park1['print_parking']('VIP')
#park1['end_parking'](100)
#park1['end_parking'](223)
#park1['print_parking']('Regular') 
