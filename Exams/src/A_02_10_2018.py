'''Task_1'''
from _ast import Nonlocal

class Tree():
    def __init__(self,value,nodes=None):
        self.value=value
        self.nodes=nodes
    def __repr__(self):
        if self.nodes:
            return 'Tree({0},{1})'.format(self.value,repr(self.nodes))
        return 'Tree({0})'.format(self.value)
        
        
def BuildTree(tree):
    if type(tree)!=tuple:
        return Tree(tree)
    nodes = list(BuildTree(branch)for branch in tree)
    return Tree(max([n.value if n.nodes !=None else 0 for n in nodes ])+1, nodes)
def SumTree(tree):
    if tree.nodes == None:
        return tree.value
    return sum(SumTree(x) for x in tree.nodes)
t1 = Tree((((2, 3), (4, (5, 6, (8, 2))))))
#print(t1.value)
t=BuildTree((((2, 3), (4, (5, 6, (8, 2)))))) 
#print(t) 
#print(SumTree(t))
'''Task_2'''

def get_Sequence(s):
    slist  =list(s)
    def all_filter(fn = lambda x:True):
        return tuple(filter(fn,slist))
    def print_filter(flag = 0, fn = lambda x:True):
        slist_temp = tuple(filter(fn,slist))
        if flag == 0:index = 0
        else: index = len(slist)-1
        def next():
            nonlocal index
            try:
                if index<0 or index>len(slist):
                    raise IndexError('Index: '+str(index)+' out of range')
            except IndexError as err:
                value  = str(err)
            else:
                value = slist_temp[index]
            finally:
                if flag == 0: index+=1
                else: index -=1
            return value
        return {'next':next}
    def extend(x):
        #nonlocal slist
        slist.extend(x)
    def clear():
        #nonlocal slist
        slist.clear()
    return {'all_filter':all_filter,'print_filter':print_filter,'clear':clear,'extend':extend}


'''
>>> list1=get_Sequence((1,2,3,4,5))
>>> list1['all_filter'](lambda x: x%2==0)
(2, 4)
>>> print1=list1['print_filter'](0,lambda x: x<4)
>>> print1['next']()
1
>>> for _ in range(5):
    print(print1['next']())
2
3
Index: 3 out of range
Index: 4 out of range
Index: 5 out of range
>>> print1=list1['print_filter'](1)
>>> for _ in range(6):
    print(print1['next']())    
5
4
3
2
1
Index: -1 out of range
>>> list1['extend'](list1['all_filter'](lambda x: x%2!=0))
>>> 
>>> list1['all_filter'](lambda x: x>2)
(3, 4, 5, 3, 5)
>>> list1['all_filter']()
(1, 2, 3, 4, 5, 1, 3, 5)
'''

'''Task_4'''
def make_class(attrs, base=None):
    def get(name):
        if name in attrs: return attrs[name]
        elif base:
# ------------------------------------------------
# alef
            for b in base:
                x=b['get'](name)
                if x:
                    return x
# ------------------------------------------------

    def set(name, value): attrs[name] = value

    def new(*args):
        attrs = {}
        def get(name):
            if name in attrs:       return attrs[name]
            else:
                value = cls['get'](name)
                if callable(value): return lambda *args: value(obj, *args)
                else:               return value

        def set(name, value):       attrs[name] = value
        obj = { 'get': get, 'set': set }
        init = get('__init__')
        if init: init(*args)

        return obj
    cls = { 'get': get, 'set': set, 'new': new }

# ------------------------------------------------
    # bet  set Base class Count
    #       or: set('BaseCount', count)
    #       or: attrs['BaseCount'] = count
    if not base: count=0
    else:
        count=len(base)
    cls['set']('BaseCount', count)
# ------------------------------------------------
    return cls

def make_classA():
    intN=2
    def strA(self):
        return 'Integer number: '+str(self['get']('intN'))+'\n'
    
    return make_class(locals())

def make_classB():
    floatN=3.5
    def strB(self):
        return 'Float number: '+str(self['get']('floatN'))+'\n'
    return make_class(locals())
A = make_classA()
B = make_classB()
def make_classC():
    def __init__(self, strN):
        self['set']('strN', strN)
# ------------------------------------------------
# gimel
    def strC(self):
        return self['get']('strA')()+self['get']('strB')()+'String: '+str(self['get']('strN'))+'\n'
# ------------------------------------------------
    return make_class(locals(),[A,B])
C= make_classC()
# ------------------------------------------------

'''
>>> c1=C['new']('test')
>>> c1['get']('intN')
2
>>> c1['get']('floatN')
3.5
>>> C['get']('BaseCount')
2
>>> A['get']('BaseCount')
0
>>> print(c1['get']('strC')())
Integer number: 2
Float number: 3.5
String: test
'''

    
    