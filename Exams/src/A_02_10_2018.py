'''Task_1'''

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
print(SumTree(t))