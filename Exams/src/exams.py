









def make_class(name, attrs, base=None):
    
    def ancestry():
        
        ##function return list of classes In order of inheritance
        ##sample run
        ##anc=CalendarEntry['get']('ancestry')()
        ##print(list(c['get']('name') for c in anc))
        #if not base:    return [cls]
        #res = base['get']('ancestry')()
        #print(res)
        #res.insert(0,cls)
        #return res
        ##OR (there are multiple alternatives):
        res = [cls]
        if base:
            res.extend(base['get']('ancestry')())
        return res
# ========================================================
# ========================================================
# ========================================================   
    #def make_instance(cls):
        #attrs = {}
        #def get(name):
            #if name in attrs:
                #return attrs[name]
            #else:
                #value = cls['get'](name)
                #if callable(value):
                    #return lambda *args: value(obj, *args)
                #else:
                    #return value
        #def set(name, value):
            #attrs[name] = value
        #obj   = { 'get': get, 'set': set }
        #obj['set']('__dict__', attrs)
        #obj['set']('__class__', cls)
        
        #return obj
    
    
    # return copy of obj
    #def clone(obj):
        ##cl = make_instance(obj['get']('__class__'))
        #OR
        #cl = make_instance(cls)
        ##for key, val in obj['get']('__dict__').items():
            ##cl['set'](key,val)
        ##return cl
    #cls['set']('__clone__', clone)
# ========================================================
# ========================================================
# ========================================================
    ## liki in JAVA --> self['get']('super')(owner) 
    #def super(ob, *args):
        #if base:
            #init  = base['get']('__init__')
            #if init: init(ob, *args)
           
# ========================================================
# ========================================================
# ========================================================
    def get(name):
        
        
        if name in attrs: return attrs[name]
        if base:
            'inheritance from different basic class'
            for b in base:
                x=b['get'](name)
                return x        
            #return base['get'](name)
            'inheritance from different basic class'
            
        raise AttributeError('Attribute {0} is not defined for {1}'.format(name, attrs['name']))
# ========================================================
    def set(name, value): attrs[name] = value
# ========================================================
    def new(*args):
        def get(name):
            if name in attrs:       return attrs[name]
            else:
                value = cls['get'](name)
                #bind_method
                if callable(value):
                    #check if function with no arguments
                    #if len((signature(value).parameters)== 0:
                           #raise TypeError('Function with no arguments cannot be bound to object')
                    return lambda *args: value(obj, *args)
                else:               return value
# ========================================================
        def set(name, value):       attrs[name] = value

        attrs = {}
        obj   = { 'get': get, 'set': set }
       
        try:
            init  = get('__init__')
            init(*args)
        except:
            print("A new instance of {0} cannot be initialized".format(cls['get']('name')))
        # type class
        # print(todo['get']('type'))
        obj['set']('type', cls['get']('name'))
        # type class
        return obj

    cls = { 'get': get, 'set': set, 'new': new }
    'count amount of base class'
    if not base: count=0
    else: count = len(base)
    attrs['BaseCount'] = count
    'count amount of base class'
    ### alef  set class name
    #       or: set('name', name)
    #       or: cls['set']('name', name)
    ##count amount of base class
    ##add name of class'
    attrs['name'] = name
    ##add name of class'
    cls['set']('ancestry', ancestry)
    
    #cls['set']('super', super)
    
    return cls
# -----------------------------------------------------------
def make_date_class():
    def __init__(self,year,month,day):
        self['set']('year',year)
        self['set']('month',month)
        self['set']('day',day)
    attributes ={'__init__':__init__}
    return make_class('make_date_class',attributes)
# -----------------------------------------------------------
def make_time_class():
    def __init__(self,hours,min):
        self['set']('hour',hours)
        self['set']('minute',min)
    def __str__(self):
        return '{0:02d}:{1:02d}'.format(self['get']('hour'),self['get']('minute'))
    return make_class('make_time_class',{'__init__':__init__ , '__str__':__str__})
# -----------------------------------------------------------
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
    
    return make_class('make_calentry_class',locals(), [Date])
# -----------------------------------------------------------
Date = make_date_class()

today=Date['new'](2017,1,20)
print( today['get']('year'))
CalendarEntry = make_calentry_class()
todo = CalendarEntry['new'](2017, 1, 20)

#print(CalendarEntry['get']('BaseCount'))
Time = make_time_class()
t = Time['new'](10,0) 
print( t['get']('__str__')() )
todo['get']('addTask')('PPL lecture', t, Time['new'](13,0)) 
todo['get']('addTask')('PPL homework#4', Time['new'](14,0), Time['new'](16,0)) 
print( todo['get']('tasks'))


