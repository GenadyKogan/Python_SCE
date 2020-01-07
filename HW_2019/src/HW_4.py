#===============================================#

                # task 1

#===============================================#
from operator import itemgetter

class Date(object):
    def __init__(self,ye,mo,da):
        self.year = ye
        self.month = mo
        self.day = da
    def __repr__ (self):
        return "Date(%s %r %d)"%(self.year,self.month,self.day)
    def __str__(self):
        months ={1:"January",2:"February", 3:"March",
                  4:"April",5:"May",6:"Juny",
                  7:"July",8:"August", 9:"September",
                  10:"October",11:"November",12:"December"}
        return "'{0}th of {1}, {2}'".format(self.day,months[self.month],self.year)
class Time():
    def __init__(self,hour,minute):
        self.hours=hour
        self.minutes=minute
    def __str__(self):
        return '{0:02d}:{1:02d}'.format(self.hours,self.minutes)   
    def __repr__(self):
        return 'Time({0:02d},{1:02d})'.format(self.hours,self.minutes)
# =================================== #
class CalendarEntry(Date):
    def __init__(self,y,m,d):
        Date.__init__(self, y, m, d)
        self.tasks={}
    def addTask(self,task,start,end):
        time=(str(start),str(end))
        for x in self.tasks:
            if x[0]==str(start) and x[1]==str(end):
                print("there is already task on this time")
                return
        self.tasks[time]=task
        #start_str,end_str=str(start),str(end)
        #self.tasks.__setitem__((start_str,end_str),task)
    def __str__(self):
        
        count=1
        
        string= 'To do list for {0}:\n'.format(Date.__str__(self))
        list = sorted(self.tasks.items(),key=itemgetter(0))
        for x in list:
            string+= '{0}. {1}-{2} - {3}\n'.format(count,x[0][0],x[0][1],x[1])
            count+=1
        
        return string 
    def __repr__(self):
        return 'CalendarEntry({0},{1},{2})'.format(self.year,self.month,self.day)
#today = Date(2017, 1, 20)
#today 
#print(today.year)
#print(today)
#todo = CalendarEntry(2017, 1, 20) 
#t = Time(10,0)
#print(str(t))
#todo.addTask('PPL lecture', t, Time(13,0))
#todo.addTask('PPL homework#4', Time(14,0), Time(16,0))
#print(todo.tasks)
#print(todo)

#===============================================#

                # task 2

#===============================================#

#class shmython    
def make_instance(cls):
    
    '''Return a new object instance, which is a dispatch dictionary.'''
    attributes = {}
    def get_value(name):
        if name in attributes:
            return attributes[name]
        else:
            value = cls['get'](name)
            #function: <function make_calentry_class.<locals>.addTask at 0x000002A1D486F1E0>
        testValue=value
        testInstance=instance
        
     
        #dict: {'get': <function make_instance.<locals>.get_value at 0x0000022DC234E400>, 'set': <function make_instance.<locals>.set_value at 0x0000022DC234E488>}
        return bind_method(value, instance)
    def set_value(name, value):
        #('year',year)
        #('month',month)
        #('day',day)
        attributes[name] = value
    instance = {'get': get_value, 'set': set_value}
    return instance

# ------------------------------------------------
def bind_method(value, instance):
    '''Return a bound method if value is callable, or value otherwise.'''
    
    if callable(value):
        #value ---> function: <function make_calentry_class.<locals>.addTask at 0x0000027901B5E1E0>
        def method(*args):
            #instance ---> dict: {'get': <function make_instance.<locals>.get_value at 0x0000027901B5E400>, 'set': <function make_instance.<locals>.set_value at 0x0000027901B5E488>}
            print()
            res=value(instance, *args)
            return res
        return method
    else:
        return value
def make_class(attributes, *base_class):
    '''Return a new class, which is a dispatch dictionary.'''
    # attributes ---> {'__init__': <function make_date_class.<locals>.__init__ at 0x000001FF7BA34F28>}
    def get_value(name):
        if name in attributes:
            return attributes[name]
        elif base_class is not None:
            return base_class['get'](name)
    def set_value(name, value):
        attributes[name] = value
       
    def new(*args):
        #args ---> (2017, 1, 20)
        #cls ---> {'get': get_value, 'set': set_value, 'new': new}
        return init_instance(cls, *args)
    cls = {'get': get_value, 'set': set_value, 'new': new}
    return cls

def init_instance(cls, *args):
    #cls ---> {'get': get_value, 'set': set_value, 'new': new}
    #args ---> (2017, 1, 20)
    '''Return a new object with type cls, initialized with args.'''
    
    instance = make_instance(cls)
    #instance ---> {'get': get_value, 'set': set_value}
    init = cls['get']('__init__')
    #cls['get']('__init__') ---> go to make_class ---> go to get_value
    #init ---> <function make_date_class.<locals>.__init__ at 0x00000220D1E64F28>
    if init:
        init(instance, *args)
       
        #instance ---> {'get': get_value, 'set': set_value}
    return instance
def make_date_class():
    def __init__(self,year,month,day):
        self['set']('year',year)
        self['set']('month',month)
        self['set']('day',day)
    attributes ={'__init__':__init__}
    return make_class(attributes)
def make_time_class():
    def __init__(self,hours,min):
        self['set']('hour',hours)
        self['set']('minute',min)
    def __str__(self):
        return '{0:02d}:{1:02d}'.format(self['get']('hour'),self['get']('minute'))
    return make_class({'__init__':__init__ , '__str__':__str__})
def make_calentry_class():
    def __init__(self,year,month,day):
        #self['set']('year',year)
        #self['set']('month',month)
        #self['set']('day',day)
        self['set']('tasks',{})
        Date['get']('__init__')(self,year,month,day)
        
    def addTask(self,task,start,end):
        time=(start['get']('__str__')(),end['get']('__str__')())
        for x in self['get']('tasks'):
            if x[0]==start['get']('__str__')() and x[1]==end['get']('__str__')():
                print("there is already task on this time")
                return
        self['get']('tasks')[time]=task
    return make_class(locals(), Date)
#Date = make_date_class()

#today=Date['new'](2017,1,20)
#print( today['get']('year'))
#CalendarEntry = make_calentry_class()
#todo = CalendarEntry['new'](2017, 1, 20) 
#Time = make_time_class()
#t = Time['new'](10,0) 
#print( t['get']('__str__')() )
#todo['get']('addTask')('PPL lecture', t, Time['new'](13,0)) 
#todo['get']('addTask')('PPL homework#4', Time['new'](14,0), Time['new'](16,0)) 
#print( todo['get']('tasks'))
#===============================================#

                # task 3

#===============================================#
rates ={('dollar', 'nis'): 3.47,('euro','nis'): 3.88,('euro','dollar'):1.12,('dollar','euro'):0.90 ,('nis','dollar'):0.29,('nis','euro'):0.26}

class Shekel():
    def __init__(self,am):
        self.amount=am
    def __str__(self):
        return '{0:.1f}nis'.format(self.amount)  
    def __repr__(self):
        return "Shekel({0:.2f})".format(self.amount)
    def __add__(self,other):
        if type(other) == Shekel:
            return  self.amount+other.amount
        return self.amount +other.amount()
class Dollar ():
    def __init__(self,am):
        self.dollar=am
    def amount(self):
        return self.dollar*rates[('dollar','nis')]    
    def __str__(self):
        return '{0:.1f}$'.format(self.dollar)  
    def __repr__(self):
        return "Dollar({0:.2f})".format(self.dollar)
    def __add__(self,other):
        if type(other) == Shekel:
            return  self.amount()+other.amount
        return self.amount() +other.amount()
        

class Euro ():
    def __init__(self,am):
        self.euro=am
    def amount(self):
        return self.euro*rates[('euro','nis')]    
    def __str__(self):
        return '{0:.1f}euro'.format(self.euro)  
    def __repr__(self):
        return "Euro({0:.2f})".format(self.euro)
    def __add__(self,other):
        if type(other) == Shekel:
            return  self.amount()+other.amount
        return self.amount() +other.amount()
#===============================================#

                # task 4

#===============================================#    
def add_shekel_dollar(sh,dol):
    return sh.amount+dol.amount()
add_dollar_shekel=lambda x,y:add_shekel_dollar(y,x)  
def add_shekel_euro(sh,eu):
    return sh.amount+eu.amount()
add_euro_shekel=lambda x,y:add_shekel_euro(y,x)
def add_dollar_euro(dol,eur):
    return dol.amount()+eur.amount()
add_euro_dollar=lambda x,y:add_dollar_euro(y,x)

                    
def sub_shekel_dollar(sh,dol):
    return sh.amount-dol.amount() 
sub_dollar_shekel=lambda x,y: -sub_shekel_dollar(y,x)
def sub_shekel_euro(sh,eu):
    return sh.amount-eu.amount()
sub_euro_shekel=lambda x,y:-sub_shekel_euro(y,x)
def sub_dollar_euro(dol,eu):
    return dol.amount()-eu.amount()
sub_euro_dollar=lambda x,y:-sub_dollar_euro(y,x)




            
def apply(operator_name, x, y):
        tags = (type_tag(x), type_tag(y))
        key = (operator_name, tags)
        return type(x)(apply.implementations[key](x, y)).__repr__()

def type_tag(x):
    return type_tag.tags[type(x)]

type_tag.tags = {Shekel: 'nis',Dollar: 'dollar', Euro: 'euro'}


apply.implementations={('add',('nis','dollar')):lambda x,y: add_shekel_dollar(x,y),
                       ('add',('nis','euro')):lambda x,y: add_shekel_euro(x,y),
                       ('add',('nis','nis')):lambda x,y: x.amount+y.amount,
                       ('add',('dollar','nis')):lambda x,y:add_dollar_shekel(x,y)/rates[('dollar', 'nis')],
                       ('add',('dollar','euro')):lambda x,y:x.dollar+(y.euro*rates[('euro','dollar')]),
                       ('add',('dollar','dollar')):lambda x,y:x.dollar+y.dollar,
                       ('add',('euro','nis')):lambda x,y:add_euro_shekel(x,y)/rates[('euro','nis')],
                       ('add',('euro','dollar')):lambda x,y:x.euro + y.dollar/rates[('euro','dollar')], 
                       ('add',('euro','euro')):lambda x,y:x.euro+y.euro,
                       ('sub',('nis','dollar')):lambda x,y: sub_shekel_dollar(x,y),
                       ('sub',('nis','euro')):lambda x,y: sub_shekel_euro(x,y),
                       ('sub',('nis','nis')):lambda x,y: x.amount-y.amount,
                       ('sub',('dollar','nis')):lambda x,y:sub_dollar_shekel(x,y)/rates[('dollar', 'nis')],
                       ('sub',('dollar','euro')):lambda x,y:x.dollar-y.euro*rates[('euro','dollar')],
                       ('sub',('dollar','dollar')):lambda x,y:x.dollar+y.dollar,
                       ('sub',('euro','nis')):lambda x,y:sub_euro_shekel(x,y)/rates[('euro','nis')],
                       ('sub',('euro','dollar')):lambda x,y:x.euro - y.dollar/rates[('euro','dollar')], 
                       ('sub',('euro','euro')):lambda x,y:x.euro-y.euro}           
#print(apply('add', Shekel(50), Dollar(20)))

rates[('euro','dollar')] = 1.06
#print(apply('add', Dollar(50), Euro(20)))
#print(apply('sub', Dollar(50), Euro(20)))
#===============================================#

                # task 5

#===============================================#
coercions={('dollar','nis'):lambda x:Shekel(x.amount()),('euro','nis'):lambda x:Shekel(x.amount()) } 
def coerce_apply(operator_name, x, y): 
    
    tx, ty = type_tag(x), type_tag(y)
    
    if tx is not 'nis' and ty is not 'nis':
        x=coercions[(tx,'nis')](x)
        y=coercions[(ty,'nis')](y)
        tx=type_tag(x)
        
    elif tx!=ty:
        if (tx, ty) in coercions:
            tx, x = ty, coercions[(tx, ty)](x)
        elif (ty, tx) in coercions:
            ty, y = tx, coercions[(ty, tx)](y)
        else:
            return 'No coercion possible.'

    
                      
    key = (operator_name, tx)
    return coerce_apply.implementations[key](x, y)

 
coerce_apply.implementations={('add','nis'):lambda x,y: repr(Shekel(x.amount+y.amount)),('sub','nis'):lambda x,y: repr(Shekel(x.amount-y.amount))}
#print( coercions[('dollar','nis')](Dollar(50)) )
#print(  coerce_apply('add', Shekel(50), Dollar(20)) )
#===============================================#

                # task 6

#===============================================#
import sys
def parking(payForHour,numRegPla,numPriorPla,numVIPPla):
    #try: 
        
        #assert payForHour > 0 # Test if it true
    #except AssertionError :
        #print("Number is negative")
    try:
        if payForHour < 0:
            raise ValueError ( "the price value is bad " )
        if numRegPla<=0 or numPriorPla<=0 or numVIPPla<=0:
            raise ValueError ( "parking places error" )
    except ValueError as e:
            print(e)
            sys.exit(1)
    listOfParking=[]
    
#===============================================#
    def print_list():
        z=0
        '''function print details of each vehicle'''
        i = len(listOfParking)
        '''def end():
            if i>0:
                return False
            else:
                return True
        def next():
            nonlocal i
            for item in listOfParking:
                print('{0}{1}{2}{3}{4}{5}'.format('car: ', item[0]  ,', parking type: ', item[1], ', parking time: ', item[2]))
                i=i-1
        return {"end":end,'next':next}'''
        def next():
            nonlocal z
            try:
                
                print(listOfParking[z][0],listOfParking[z][1])
            
                z=z+1
                if z>i:
                    raise IndexError 
            except IndexError :
                print("no car")
            
        return {'next':next}
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
        #print('value --->',value) or value!='VIP' or value !='Priority'
        try:
            if type(key) != int:
                raise TypeError ('incorrect car number')
            if value!='Regular' and  value!='VIP' and value !='Priority':
                raise TypeError(value+' is incorrect prking type')
            
        except TypeError as e:
            print(e)
        else:    
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

#park1=parking(10,3,3,3) 
#print( park1 )
#park1['start_parking']('aaa','Regular') 
#park1['start_parking'](223,'VIP1')
#park1['start_parking'](222,'Regular')
#park1['start_parking'](223,'Regular')
#park1['next_time']() 
#park1['start_parking'](224,'Regular')
#park1['start_parking'](225,'VIP') 
#prn=park1['print_list']()
#print(prn)
'''while not prn['end']():  
    prn['next']()'''
#for _ in range(6):
    #prn['next']()
#park1['print_parking']('VIP')
#park1['end_parking'](100)
#park1['end_parking'](223)
#park1['print_parking']('Regular') 






#===============================================#

                # task 9

#===============================================#

from functools import reduce
from operator import mul,add
from math import sqrt

def repl():
    
    while True:
        try:
            expression_tree = calc_parse(input('calc> '))                    
            print(calc_eval(expression_tree))
        #### new errors: ValueError, ArithmeticError ####
        except (SyntaxError, TypeError, ValueError, ArithmeticError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):  # <Control>-D, etc. <ctrl-C>
            print('Calculation completed.')
            return

## Eval & Apply

class Exp(object):
    def __init__(self, operator, operands):
        self.operator = operator
        self.operands = operands

    def __repr__(self):
        return 'Exp({0}, {1})'.format(repr(self.operator), repr(self.operands))

    def __str__(self):
        operand_strs = ', '.join(map(str, self.operands))
        return '{0}({1})'.format(self.operator, operand_strs)

def calc_eval(exp):
    if type(exp) in (int, float):
        return exp
    if type(exp) == Exp:
        arguments = list(map(calc_eval, exp.operands))
        return calc_apply(exp.operator, arguments)
    ##### sequence ###
    if type(exp) == list:
          return list(map(calc_eval, exp))
    
def calc_apply(operator, args):
    if operator in ('add', '+'):
        return sum(args)
    if operator in ('sub', '-'):
        if len(args) == 0:
            raise TypeError(operator + 'requires at least 1 argument')
        if len(args) == 1:
            return -args[0]
        return sum(args[:1] + [-arg for arg in args[1:]])
    if operator in ('mul', '*'):
        #new test
        if len(args) == 0:
            raise TypeError(operator + 'requires at least 1 argument')
        return reduce(mul, args, 1)
    if operator in ('div', '/'):
        if len(args) != 2:
            raise TypeError(operator + ' requires exactly 2 arguments')
        #numer, denom = args
        #returns infinite if denominator = 0
####        if denom == 0: return float("inf")
####        return float(numer)/denom
        #OR:
        try:
                return args[0]/args[1]
        except ZeroDivisionError as s:
                return float("inf")
    #### new operator - round ####
    if operator == 'round':
        if len(args) != 2:
            raise TypeError(operator + ' requires exactly 2 arguments')
        base, prec = args
        return round(base, prec)
    
### Parsing

def calc_parse(line):
    tokens = tokenize(line)
    #### sequence of commands ####
    if ';' in tokens:
        result = []
        while ';' in tokens:
            token = tokens[0:tokens.index(';')]
            result.append(analyze(token))
            tokens = tokens[tokens.index(';')+1:]
    else:
    ##############################
            result = analyze(tokens)
    if len(tokens) > 0:
        raise SyntaxError('Extra token(s): ' + ' '.join(tokens))
    return result

def tokenize(line):
    #### add token ';' ###
    spaced = line.replace('(',' ( ').replace(')',' ) ').replace(',', ' , ').replace(';',' ; ')
    return spaced.strip().split()

###new operator: 'round'
known_operators = ['round', 'add', 'sub', 'mul', 'div', 'pow', 'sqrt', '+', '-', '*', '/', '^', 'V']

def analyze(tokens):
    assert_non_empty(tokens)
    token = analyze_token(tokens.pop(0))
    if type(token) in (int, float):
        return token
    if token in known_operators:
        if len(tokens) == 0 or tokens.pop(0) != '(':
            raise SyntaxError('expected ( after ' + token)
        return Exp(token, analyze_operands(tokens))
    else:
        return token
        
def analyze_operands(tokens):
    assert_non_empty(tokens)
    operands = []
    while tokens[0] != ')':
        if operands and tokens.pop(0) != ',':
            raise SyntaxError('expected ,')
        operands.append(analyze(tokens))
        assert_non_empty(tokens)
    tokens.pop(0)  # Remove )
    return operands

def assert_non_empty(tokens):
    if len(tokens) == 0:
        raise SyntaxError('unexpected end of line')

def analyze_token(token):
    try:
        return int(token)
    except (TypeError, ValueError):
        try:
            return float(token)
        except (TypeError, ValueError):
            return token
repl()
####OUTPUT examples#####
# calc> round(div(1,6),3)