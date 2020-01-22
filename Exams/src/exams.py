def make_class(name, attrs, base=None):
#########
    def make_instance(cls):
        attrs = {}
        def get(name):
            if name in attrs:
                return attrs[name]
            else:
                value = cls['get'](name)
                ####e####
                if value:
                #########
                    if callable(value):
                        return lambda *args: value(obj, *args)
                    else:
                        return value
                ####e####
                else:
                    raise AttributeError('\''+cls['__name__']+'\' object has no attribute \''+name+'\'')
                #########
        def set(name, value):
            ####b####
            attr = cls['get'](name)
            if attr:
                raise AttributeError('static field \''+name+'\' cannot be overridden')
            #########

            ####c####
            if callable(value):
                raise AttributeError('instance attribute \''+name+'\' cannot be function')
            #########

            ####a####
            if name in attrs:
                print('attribute \''+name+'\' was updated from \''+attrs[name]+'\' to \''+value+'\'')
            #########
            attrs[name] = value
        obj   = { 'get': get, 'set': set }
        return obj
    def get(name):
        if name in attrs: return attrs[name]
        elif base:        return base['get'](name)
    def set(name, value): attrs[name] = value
    def new(*args):
        inst = make_instance(cls)
        init  = cls['get']('__init__')
        if init: init(inst, *args)
        return inst
    ####d####
    #__name__ - an additional message
    cls = { 'get': get, 'set': set, 'new': new, '__name__':name}
    #########
    return cls

def make_account_class():
    def __init__(self, owner):
        self['set']('owner', owner)
        self['set']('balance',0)
    return make_class('Account', { '__init__' : __init__ , 'interest' : 0.01})

Account = make_account_class()
Jim = Account['new']('Jim')
Jim['set']('owner','Jimmy')
# attribute owner was updated from Jim to Jimmy
Jim['get']('owner')
# 'Jimmy'
Jim['set']('address','B7')
Jim['get']('address')
# 'B7'
#Jim['set']('interest',0.02)
##Traceback (most recent call last):
##  File "<pyshell#19>", line 1, in <module>
##    Jim['set']('interest',0.02)
##  ....
##AttributeError: static field 'interest' cannot be overridden
#Jim['set']('withdraw',lambda x: 100)
##Traceback (most recent call last):
##  File "<pyshell#21>", line 1, in <module>
##    Jim['set']('withdraw',lambda x: 100)
##  ....
##AttributeError: instance attribute 'withdraw' cannot be function
Account['__name__']
# 'Account'
Jim['get']('stam')
##Traceback (most recent call last):
##  File "<pyshell#18>", line 1, in <module>
##    Jim['get']('stam')
##  ....
##AttributeError: 'Account' object has no attribute 'stam'




