'''Task_1'''
from _ast import While
class Expr():
    def __init__(self,entry,left,right):
        self.entry = entry
        self.left = left
        self.right = right
    def __repr__(self):
        return "Expr({0},{1},{2})".format(repr(self.entry),
                                          repr(self.left),repr(self.right))
    
def build_expr_tree(tree):
    if type(tree)!=tuple:return tree
    return Expr(tree[0],build_expr_tree(tree[2]),build_expr_tree(tree[2]))

exp = build_expr_tree(('add', ('mul', 2, 3), 10))
#print(exp) 

'''Task_2'''

def test_eval_order():
    return 10

def never_ends(f):
    while True:
        print("Never Ends")
        
#print(never_ends(test_eval_order()))

'''Task_5'''

### [Appendix: Shmython]
'''def make_class(attrs, base=None):
    def make_instance(cls):
        attrs = {}
        def get(name):
            if name in attrs:
                return attrs[name]
            else:
                value = cls['get'](name)
                if callable(value):
                    return lambda *args: value(obj, *args)
                else:
                    return value
        def set(name, value):
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
    cls = { 'get': get, 'set': set, 'new': new }
    return cls'''
### [End of Shmython]

def make_class(name,attrs, base=None):
    def make_instance(cls):
        attrs = {}
        def get(name):
            if name in attrs:
                return attrs[name]
            else:
                value = cls['get'](name)
                if value:
                #########
                    if callable(value):
                        return lambda *args: value(obj, *args)
                    else:
                        return value
                #e
                else:
                    raise AttributeError('\''+cls['__name__']+'\' object has no attribute \''+name+'\'')
                #########
        def set(name, value):
            #b??:
            attr = cls['get'](name)
            if attr:
                raise AttributeError('static field \''+name+'\' cannot be overridden')
            #c:
            if callable(value):
                raise AttributeError('instance attribute \''+name+'\' cannot be function')
            #a:
            if name in attrs:
                print('attribute \''+name+'\' was updated from \''+attrs[name]+'\' to \''+value+'\'')
            attrs[name] = value
        obj   = { 'get': get, 'set': set }
        return obj
    def get(name):
        if name in attrs: 
            return attrs[name]
        elif base:  
            return base['get'](name)
    def set(name, value): 
        attrs[name] = value
    def new(*args):
        inst = make_instance(cls)
        init  = cls['get']('__init__')
        if init: init(inst, *args)
        return inst
    cls = { 'get': get, 'set': set, 'new': new }
    # d:  set class name
        #or: set('name', name)
        #or: attrs['name'] = name
        #or: cls['set']('name', name)
        #or:
    cls = { 'get': get, 'set': set, 'new': new, '__name__':name}   
    return cls

def make_account_class():
    def __init__(self, owner):
        self['set']('owner', owner)
        self['set']('balance',0)
    return make_class('Account', { '__init__' : __init__ , 'interest' : 0.01})

Account = make_account_class()
Jim = Account['new']('Jim')
print(Jim['get']('stam'))