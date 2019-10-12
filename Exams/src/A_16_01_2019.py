'''========================================================================================='''       
'''Task_1'''
from functools import reduce

class Tree():
    def __init__(self,entry,nodes=None):
        self.entry = entry
        self.nodes = nodes
        self.leaf = not nodes
        self.binary = nodes != None and len(nodes)==2 and (nodes[0].leaf or nodes[0].binary) and (nodes[1].leaf or nodes[1].binary)
    def __repr__(self):
        if self.nodes: 
            return 'Tree ({0},{1})'.format(self.entry,repr(self.nodes) )
        return 'Tree ({0})'.format(self.entry)
def merge_trees(g,*trees):
    return Tree(reduce(g,(n.entry for n in trees)),trees)
def safe_merge_trees(g,*trees):
    try:
        return merge_trees(g,*trees)
    except TypeError as err:
        print(err)
'''t1, t2 = Tree(1), Tree(2)
print(t2.leaf)
print(t2.binary)
t3 = merge_trees(lambda x,y:x+y,t1,t2)
print(t3)
print(t3.leaf)
print(t3.binary)
t3 = merge_trees(lambda x,y:x*y,t3,t3)
print(t3)
print(t3.leaf)
print(t3.binary)
safe_merge_trees(sum,t1,t3)
safe_merge_trees(lambda x,y:x*y)
safe_merge_trees(lambda x,y:x*y,t1)'''
        
'''========================================================================================='''       
'''Task_3'''
#1
lambda x,y:lambda z:x+y if z==1 else pow(x,y)(1,2)(3)
def foo(x,y):
    def goo(z):
        return x+y if z==1 else pow(x,y)
    return goo
'''print(foo(1,2)(4))'''
'''========================================================================================='''     

'''Task_4'''

### [Appendix: Shmython]
def make_class(name,attrs, base=None):
    def get(name):
        if name in attrs: return attrs[name]
        elif base:        return base['get'](name)
    def set(name, value): attrs[name] = value

    def new(*args):
        def get(name):
            if name in attrs:       return attrs[name]
            else:
                value = cls['get'](name)
                if callable(value): return lambda *args: value(obj, *args)
                else:               return value
        def set(name, value):       attrs[name] = value

        attrs = {}
        obj   = { 'get': get, 'set': set }
        init  = get('__init__')
        if init: init(*args)
        return obj
    # alef  set class name
    
    cls = { 'get': get, 'set': set, 'new': new,'name':name }
    return cls
### [End of Shmython]
def make_account_class():     
        return make_class('Account', {'interest' : 0.05}) 
def make_save_account_class():    
        return make_class('SaveAccount', {'interest' : 0.03}, Account) 

Account = make_account_class() 
SaveAccount = make_save_account_class() 
