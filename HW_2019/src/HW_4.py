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
class Shekel(object):
    def __init__(self,am):
        self.shekel=am
    def amount(self):
        return self.shekel
    def __str__(self):
        return '{0:.1f}nis'.format(self.shekel)  
    def __repr__(self):
        return "Shekel({0:.2f})".format(self.amount())
    def __add__(self,other):
        if type(other) == Shekel:
            return  self.shekel+other.shekel
        return self.shekel +other.shekel()

class Dollar (object):
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
        

class Euro (object):
    def __init__(self,am):
        self.euro=am
    def amount(self):
        return self.euro*rates[('euro','nis')]    
    def __str__(self):
        return '{0:.1f}{1}'.format(self.euro,chr(8364))  
    def __repr__(self):
        return "Euro({0:.2f})".format(self.euro)
    def __add__(self,other):
        if type(other) == Shekel:
            return  self.amount()+other.amount
        return self.amount() +other.amount()
def add(z1,z2):return z1.amount()+z2.amount()
def sub (z1,z2): return z1.amount() -z2.amount()
#s = Shekel(50)
#d = Dollar(50)
#e = Euro(50) 
#print(d.amount())
#print(e.amount())
#print(d + s)
#print(add(e,d))
#z=eval(repr(d))
#print(repr(d))
#print(z)
#print(s)
#print(e)
#===============================================#

                # task 4

#===============================================#
def add_shekel_dollar(sh,dol):
    
    return sh.amount()+dol.amount()
add_dollar_shekel=lambda x,y:add_shekel_dollar(y,x)  
def add_shekel_euro(sh,eu):
    return sh.amount()+eu.amount()
add_euro_shekel=lambda x,y:add_shekel_euro(y,x)
def add_dollar_euro(dol,eur):
    return dol.amount()+eur.amount()
add_euro_dollar=lambda x,y:add_dollar_euro(y,x)

                    
def sub_shekel_dollar(sh,dol):
    return sh.amount()-dol.amount()
sub_dollar_shekel=lambda x,y: -sub_shekel_dollar(y,x)
def sub_shekel_euro(sh,eu):
    return sh.amount()-eu.amount()
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
        
        
print(apply('add',  Dollar(20),Shekel(50)))
#Shekel(131.4)
#rates[('euro','dollar')] = 1.06
print(apply('add', Dollar(50), Euro(20)))
print(apply('sub', Dollar(50), Euro(20)))
#===============================================#

                # task 4

#===============================================#