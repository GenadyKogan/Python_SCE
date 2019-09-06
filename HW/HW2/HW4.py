#task 1 =================================================== task 1#
print("#task 1 =================================================== task 1#")
from datetime import time

class Date(object):#class Date(date):
    #mydate = "%Y %m %d"
# =================================== #
    def __init__(self,ye,mo,da):
        self.year = ye
        self.month = mo
        self.day = da
        #self.date = self.mydate
# =================================== #
    def __repr__ (self):
        return "Date(%s %r %d)"%(self.year,self.month,self.day)
        #return self.strftime(self.date)
        #return "Date({0},{1},{2})".format(self.year,self.month,self.day)
# =================================== #    
    def __str__(self):
        months ={1:"January",2:"February", 3:"March", 4:"April",5:"May",6:"Juny",7:"July",8:"August", 9:"September",10:"October",11:"November",12:"December"}
        return "'{0}th of {1}, {2}'".format(self.day,months[self.month],self.year)
    #def __str__(self):
        #print("________str________date")
        #return self.strftime("%d th of %b, %Y")
        
class Time(time): 
    
    #myTime= "%H %M"
# =================================== #    
    #def __init__(self,hour=0,minute=0):
        #self.time = self.myTime
    #def __repr__ (self):
       #return self.strftime(self.time)
    #def __str__ (self): 
       #return self.strftime("%H:%M")
# =================================== #
    def __init__(self,hh,mm):
        self.hours =hh
        self.minutes = mm
    def __repr__(self):
        return "Time({0:02d},{1:02d})".format(self.hours, self.minutes)
    def __str__(self):
        return "{0:02d}:{1:02d}".format(self.hours, self.minutes)

class  CalendarEntry():
    tasks={}
# =================================== #
    def __init__(self,year=0000,month=0,day=0,hour=0,minute=0):
        self.date=Date(year,month,day)
        self.time=Time(hour,minute)
# =================================== #        
    def addTask(self,task,start,end):
        start_str,end_str=str(start),str(end)
        self.tasks.__setitem__((start_str,end_str),task) #self.task.__setitem__(key, value)
        
# =================================== #        
    def __str__(self):  
        return  "Todo list for "+str(self.date)+'\n'+str(self.tasks) 
# =================================== #
    
today = Date(2017, 1, 20)
#today 
print(today.year) 
print(today)
todo = CalendarEntry(2017, 1, 20) 
t=Time(10,0)
print(str(t))
todo.addTask("PPL lecture", t, Time(13,0)) 
todo.addTask("PPL homework4", Time(14,0), Time(16,0))
print(todo.tasks)
print(todo)

#task 2 =================================================== task 2
print("#task 2 =================================================== task 2#")
def bind_method(value, instance):
    #Return a bound method if value is callable, or value otherwise.
    if callable(value):
        def method(*args):
            return value(instance, *args)
        return method
    else:
        return value
#==============================================# 
def make_instance(cls):
    #Return a new object instance, which is a dispatch dictionary.
    attributes = {}
    def get_value(name):
        if name in attributes:
            return attributes[name]
        else:
            value = cls['get'](name)
            return bind_method(value, instance)
    def set_value(name, value):
        attributes[name] = value
    instance = {'get': get_value, 'set': set_value}
    return instance
#==============================================# 
def make_class(attributes, base_class=None):
        #Return a new class, which is a dispatch dictionary.
        def get_value(name):
            if name in attributes:
                return attributes[name]
            elif base_class is not None:
                return base_class['get'](name)
        def set_value(name, value):
            attributes[name] = value
        def new(*args):
            return init_instance(cls, *args)
        cls = {'get': get_value, 'set': set_value, 'new': new}
        return cls
#==============================================# 
def init_instance(cls, *args):
    #Return a new object with type cls, initialized with args.
    instance = make_instance(cls)
    init = cls['get']('__init__')
    if init:
        init(instance, *args)
    return instance#
#==============================================#
#==============================================#   
def newDate(y,m,d):
    def get(massage):
        if massage == "year":
            return y
        if massage == "month":
            return m
        if massage == "day":
            return d
        if massage == "__str__":
            return "'{0}th of {1}, {2}'".format(d,m,y) 
    
    return {'get':get}
#==============================================#   
def make_date_class():
    return {"new":newDate}
#==============================================#   

def make_time_class():
    def __init__(self,h,m):
        self['set']('hours',h)
        self['set']('minutes',m)
    def __str__(self):
        return "{0:02d}:{1:02d}".format(self['get']('hours'),self['get']('minutes'))
    return make_class({"__init__":__init__,'__str__':__str__})
#==============================================# 
def make_calentry_class():
 
    def __init__(self,y,m,d):
        self['set']('year', y)
        self['set']('month', m)
        self['set']('day', d)
        self['set']('tasks',{})

    def addTask(self,task,start,end):
        #task = {}
        
        key = (str(start['get']('__str__')()), str(end['get']('__str__')()))
        tasks = self['get']('tasks')
        if  key not in tasks:
            self['get']('tasks')[key] = task
        else:
            print("Time {0} exists in tasks list".format(key))
    return make_class(locals())
    
#==============================================# 
#==============================================# 
  
Date = make_date_class()       
today = Date['new'](2017, 1, 20)
print(today['get']("__str__"))
CalendarEntry = make_calentry_class()
todo = CalendarEntry["new"](2017, 1, 20)
Time = make_time_class()
t = Time['new'](10,0)
print(t['get']('__str__')())
todo['get']('addTask')("PPL lecture", t, Time['new'](13,0)) 
todo['get']('addTask')("PPL homework#4", Time['new'](14,0), Time['new'](16,0))
print(todo['get']('tasks'))
#==============================================#


#task 3 =================================================== task 3
print("#task 3 =================================================== task 3#")
def add(z1,z2):
    y=z1.amount()
    x=z2.amount()
    #print(x+y)
    return x+y

def sub (z1,z2):
   
    y=z1.amount()
    x=z2.amount()
    return y-x
#==============================================#
class Shekel(object):
    
    def __init__(self,shekel):
        self.shekel=shekel
        
    def __str__(self):
        return "{0:.2f} nis".format(self.shekel)
    def __repr__(self):
        #x=str(self.shekel)
        #return x
        return "Shekel({0:02.2f})".format(self.shekel)
    def amount(self):
        return self.shekel
    
    def __add__(self, other):
        return add(self, other)
    def __sub__(self,other):
        return sub(self,other)
#==============================================#    
    
#s = Shekel(50)
#d= Shekel(50)
#print(s.amount())
#s= add(s,d)
#print(s)
#==============================================#
class Dollar(object):
  
   
    def __init__(self,dollars):
        self.dollars = dollars

    def amount(self):
        return self.dollars * rates[('dollar','nis')]

    def __add__(self,other):
        return self.amount() + other.amount()

    def __repr__(self):
        return "Dollar({0:02.2f})".format(self.dollars)

    def __str__(self):
        return "{0:.2f}$".format(self.dollars)
#==============================================#

class Euro(object):
    def __init__(self,euro):
        self.euro = euro
    def amount(self):
        return self.euro * rates[('euro','nis')]
    def __add__(self,other):
        return self.amount() + other.amount()
    def __str__(self):
        return "{0:.2f}$".format(self.euro)
    def __repr__(self):
        return "Dollar({0:02.2f})".format(self.euro)  
#==============================================#

rates ={('dollar', 'nis'): 3.82,('euro','nis'): 4.07}

s = Shekel(50)
d = Dollar(50)
e = Euro(50)
print(d.amount())
#191.18
print( e.amount())
#203.51
print(d + s)
#241.18

print(add(e, d))
#394.69
z=eval(repr(d))
print(z)
#50.0$
print(s)
#50.0nis
print(e)


#task 4 =================================================== task 4#
print("#task 4 =================================================== task 4#")
def type_tag(x):
    return type_tag.tags[type(x)]
type_tag.tags = {Euro: 'euro', Dollar: 'dollar', Shekel: 'nis'}

#==============================================#
def Sum2Elem(x,y):
    return x+y
def Sub2Elem(x,y):
    return x-y
def apply(operator_name, x, y):
    types=(type_tag(x),type_tag(y))
    if operator_name=='add':
        
        if types==('nis','euro'):
            num=str(Sum2Elem(x,y))
            return "Shekel({0})".format(num)
        if types==('nis','dollar'):
            num=str(Sum2Elem(x,y))
            return "Shekel({0})".format(num)
        if types==('dollar','dollar'):
            num=str(Sum2Elem(x,y)/rates[('dollar', 'nis')])
            return "Dollar ({0})".format(num)
        if types==('dollar','nis'):
            num=str(Sum2Elem(x,y)/rates[('dollar', 'nis')])
            return "Dollar ({0})".format(num)
        if types==('nis','nis'):
            num=str(Sum2Elem(x,y))
        if types==('euro','nis'):
            num=str((Sum2Elem(x,y))(Sum2Elem(x,y))/rates[('euro','nis')])
            return "Euro ({0})".format(num)
        if types==('dollar','euro'):
            num=str((Sum2Elem(x,y))/rates[('dollar', 'nis')])
            return "Dollar ({0})".format(num)
            return "Shekel({0})".format(num)
        if types==('euro','euro'):
            num=str((Sum2Elem(x,y))/rates[('euro','nis')])
            return "Euro ({0})".format(num)
        if types==('euro','dollar'):
            num=str((Sum2Elem(x,y))/(Sum2Elem(x,y))/rates[('euro','nis')])
            return "Euro ({0})".format(num)
        
#==============================================#        
        
    if operator_name=='sub':
        if types==('nis','euro'):
            num=str(x-y)
            return "Shekel({0})".format(num)
        if types==('nis','dollar'):
            num=str(Sub2Elem(x,y))
            return "Shekel({0})".format(num)
        if types==('euro','dollar'):
            num=str((Sub2Elem(x,y)) /rates[('euro','nis')])
            return "Euro ({0})".format(num)
        if types==('euro','nis'):
            num=str((Sub2Elem(x,y)) /rates[('euro','nis')])
            return "Euro ({0})".format(num)
        if types==('nis','nis'):
            num=str(Sub2Elem(x,y))
            return "Shekel({0})".format(num)
        if types==('euro','euro'):
            num=str((Sub2Elem(x,y))/rates[('euro','nis')])
            return "Euro ({0})".format(num)
        if types==('dollar','nis'):
            num=str((Sub2Elem(x,y))/rates[('dollar', 'nis')])
            return "Dollar ({0})".format(num)
        if types==('dollar','euro'):
            num=str((Sub2Elem(x,y))/rates[('dollar', 'nis')])
            return "Dollar ({0})".format(num)
        if types==('dollar','dollar'):
            num=str((Sub2Elem(x,y)) /rates[('dollar', 'nis')])
            return "Dollar ({0})".format(num)
        
        
print(apply('add', Shekel(50), Dollar(20)))
#Shekel(131.4)
rates[('euro','dollar')] = 1.06
print(apply('add', Dollar(50), Euro(20)))

#task 5 =================================================== task 5#
print("#task 5 =================================================== task 5#")
def DolShek(x):
    return "Shekel({0})".format(x.dollars*rates[('dollar', 'nis')])
     
def EuroShek(x):
    return x.euro*rates[('euro', 'nis')]
def coerce_apply(operator_name, x, y):
  
    tx, ty = type_tag(x), type_tag(y)
    if type_tag(x) != type_tag(y):
        if (type_tag(x) or type_tag(y)) in coercions:
            tx, x = type_tag(y), coercions[(type_tag(x), type_tag(y))](x)
        if (ty or tx) in coercions:
            ty, y = tx, coercions[(type_tag(y), type_tag(x))](y)
        
    
   
    return coerce_apply.implementations[operator_name, tx](x, y)

coercions={('dollar','nis'):lambda x: print( DolShek(x)) ,
           ('euro','nis'):lambda x:print(EuroShek(x))}


x=coercions[('dollar','nis')](Dollar(50))
print(x)
#Shekel(191.18)
print(apply('add', Shekel(50), Dollar(20)))

#task 6 =================================================== task 6#
print("#task 6 =================================================== task 6#")
def get_reverse_map_iterator(s, g=None):
    i = len(s)-1
    # a
    def next():
        
        nonlocal i
        try:    
            if has_more():
                i -=1
            #print("index in fun next",i)
                return g(s[i+1])
            else:
                return "no more items"
        except(ArithmeticError, ValueError, TypeError, IndexError) as error:
            return next()
    # b
    def has_more():
        
        if i != -1:
            #print("index in fun has_more",i)
            return True
        else:
            return False

    dispatch = {"next": next, "has_more": has_more}
    
    return dispatch

it = get_reverse_map_iterator((1,0,6), lambda x: 1/x)
while it['has_more']():
    print(it['next']())
it = get_reverse_map_iterator((1,'a',6), lambda x: x-0)
for _ in range(1,4):
    print(it['next']())
    
#task 7 =================================================== task 7#
print("#task 7 =================================================== task 7#")
from functools import reduce
from operator import mul,add
from math import sqrt,pow
#==============================================#

def read_eval_print_loop():
    #Run a read-eval-print loop for calculator.
    while True:
        try:
            expression_tree = calc_parse(input('calc> ' ))
            print(calc_eval(expression_tree))
        except(SyntaxError, TypeError, ZeroDivisionError,ValueError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError): 
            print('Calculation completed.')
            return

#==============================================#

class Exp(object):
    """A call expression in Calculator.
    
    >>> Exp('add', [1, 2])
    Exp('add', [1, 2])

    >>> str(Exp('add', [1, Exp('mul', [2, 3])]))
    'add(1, mul(2, 3))'
    """

    def __init__(self, operator, operands):
        self.operator = operator
        self.operands = operands

    def __repr__(self):
        return 'Exp({0}, {1})'.format(repr(self.operator), repr(self.operands))

    def __str__(self):
        operand_strs = ', '.join(map(str, self.operands))
        return '{0}({1})'.format(self.operator, operand_strs)
#==============================================#

def calc_eval(exp):
    #evaluate a calculator
    if type(exp) in (int, float):
        return exp
    if type(exp) == Exp:
        arguments = list(map(calc_eval, exp.operands))
        return calc_apply(exp.operator, arguments)
 #==============================================#
   
def calc_apply(operator, args):
    if operator in ('add', '+'):
        return sum(args)
    if operator in ('sub', '-'):
        if len(args) == 0:
            raise TypeError(operator + ' requires at least 1 argument')
        if len(args) == 1:
            return -args[0]
        return sum(args[:1] + [-arg for arg in args[1:]])
    if operator in ('mul', '*'):
        return reduce(mul, args, 1)
    if operator in ('div', '/'):
        if len(args) != 2:
            raise TypeError(operator + ' requires exactly 2 arguments')
        numer, denom = args
        return numer/denom
    if operator in ('pow', '^'):
        if len(args)!=1 and len(args) !=2:
            raise TypeError(operator + ' requires exactly 2 arguments')
        if len(args)==1:    
            return args[0]**2
        if len(args)==2:
            return args[0]**args[1]
    if operator in ('sqrt', 'V'):
        if args[0]>0:
            return args[0]*0.5
        if args[0]<0:
            raise ValueError(operator+'math domain error')
        if len(args)!=1:
            raise TypeError(operator+ 'requires at least 1 argument')
    

#==============================================#

def calc_parse(line):
    tokens = tokenize(line)
    result = analyze(tokens)
    if len(tokens) > 0:
        raise SyntaxError('Extra token(s): ' + ' '.join(tokens))
    return result
#==============================================#

def tokenize(line):
    """Convert a string into a list of tokens.
    
    >>> tokenize('add(2, mul(4, 6))')
    ['add', '(', '2', ',', 'mul', '(', '4', ',', '6', ')', ')']
    """
    spaced = line.replace('(',' ( ').replace(')',' ) ').replace(',', ' , ').replace('=', ' = ')
    return spaced.strip().split()


#==============================================#


known_operators = ['add', 'sub', 'mul', 'div', 'sqrt','pow', '+', '-', '*', '/', 'V', '^']
#==============================================#


def analyze(tokens):
    """Create a tree of nested lists from a sequence of tokens.

    Operand expressions can be separated by commas, spaces, or both.
    
    >>> analyze(tokenize('add(2, mul(4, 6))'))
    Exp('add', [2, Exp('mul', [4, 6])])
    >>> analyze(tokenize('mul(add(2, mul(4, 6)), add(3, 5))'))
    Exp('mul', [Exp('add', [2, Exp('mul', [4, 6])]), Exp('add', [3, 5])])
    """
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
        
        #raise SyntaxError('unexpected ' + token)
#==============================================#
        
def analyze_operands(tokens):
    assert_non_empty(tokens)
    operands = []
    while tokens[0] != ')':
        if operands and tokens.pop(0) != ',':
            raise SyntaxError('expected ,')
        operands.append(analyze(tokens))
        assert_non_empty(tokens)
    tokens.pop(0)
    return operands
#==============================================#

def assert_non_empty(tokens):
    """Raise an exception if tokens is empty."""
    if len(tokens) == 0:
        raise SyntaxError('unexpected end of line')
#==============================================#

def analyze_token(token):
    """Return the value of token if it can be analyzed as a number, or token.
    
    >>> analyze_token('12')
    12
    >>> analyze_token('7.5')
    7.5
    >>> analyze_token('add')
    'add'
    """
    try:
        return int(token)
    except (TypeError, ValueError):
        try:
            return float(token)
        except (TypeError, ValueError):
            return token
#==============================================#

def run():
    read_eval_print_loop()

run()
