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

# ------------------------------------------------
def init_instance(cls, *args):
    '''Return a new object with type cls, initialized with args.'''
    instance = make_instance(cls)
    init = cls['get']('__init__')
    if init:
        init(instance, *args)
    return instance
def make_date_class():
    def __init__(self,year,month,day):
        self['set']('year',year)
        self['set']('month',month)
        self['set']('day',day)
    return make_class({'__init__':__init__})
def make_time_class():
    def __init__(self,hours,min):
        self['set']('hour',hours)
        self['set']('minute',min)
    def __str__(self):
        return '{0:02d}:{1:02d}'.format(self['get']('hour'),self['get']('minute'))     
    return make_class({'__init__':__init__ , '__str__':__str__})
def make_calentry_class():  
    def __init__(self,year,month,day):
        date['get']('__init__')(self,year,month,day)
        tasks={}
        self['set']('tasks',tasks)
    def  addTask(self,name,start,end): 
         
        time=(start['get']('__str__')(),end['get']('__str__')())
     
        for x in self['get']('tasks'):
            if x[0]==start['get']('__str__')() and x[1]==end['get']('__str__')():
                print("there is already task on this time")
                return
      

        self['get']('tasks')[time]=name
        
         
    return make_class(locals(),date)

date= make_date_class()
