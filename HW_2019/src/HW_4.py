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
        def method(*args):
            return value(instance, *args)
        return method
    else:
        return value
def make_class(attributes, base_class=None):
    '''Return a new class, which is a dispatch dictionary.'''
    # attributes ---> {'__init__': <function make_date_class.<locals>.__init__ at 0x000001FF7BA34F28>}
    def get_value(name):
        if name in attributes:
            return attributes[name]
        elif base_class is not None:
            return base_class['get'](name)
    def set_value(name, value):
        attributes[name] = value
        "?????" 
    def new(*args):
        #args ---> (2017, 1, 20)
        #cls ---> {'get': get_value, 'set': set_value, 'new': new}
        return init_instance(cls, *args)
    cls = {'get': get_value, 'set': set_value, 'new': new}
    return cls

# ------------------------------------------------
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
Date = make_date_class()
# Date ---> {'get': get_value, 'set': set_value, 'new': new}
today=Date['new'](2017,1,20)
print( today['get']('year'))

Time = make_time_class() 
t = Time['new'](10,0)
print(t['get']('__str__')()) 