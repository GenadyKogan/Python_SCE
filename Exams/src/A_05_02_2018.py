'''Task_1'''
from _functools import reduce
class Tree():
    def __init__(self,entry, nodes=None):
        self.entry = entry
        self.nodes = nodes
    def __repr__(self):
        if self.nodes:
            return 'Tree({0},{1})'.format(self.entry,repr(self.nodes))
        return 'Tree({0})'.format(self.entry)
    
def map_transform(tree,g=lambda x,y:x+y):
    if type(tree)!= tuple:
        return Tree(tree)
    
    nodes = list(map_transform(branch, g) for branch in tree)
    
    return Tree(reduce(g,(n.entry for n in nodes)),nodes)
        
def safe_map_transform(tree,g):
    try:
        map_transform(tree, g)
    except TypeError as fee:
        print(fee)

'''print(map_transform(((2, 3), (4, (5, 6)))))
Tree(20,[Tree(5,[Tree(2), Tree(3)]), Tree(15,[Tree(4), Tree(11,[Tree(5), Tree(6)])])])
print(map_transform(((2, 3), (4, (5, 6, (8, 2)))),lambda x,y: x if x>y else y))
Tree(8,[Tree(3,[Tree(2), Tree(3)]), Tree(8,[Tree(4), Tree(8,[Tree(5), Tree(6), Tree(8,[Tree(8), Tree(2)])])])])
print(safe_map_transform(((2, 'a'), (4, (8, 2))),min))'''
