#task 4
def Make_iterator(fn):
    x=0
    def foo(): 
        nonlocal x 
        res = fn(x)
        x+=1
        return res
    return foo

fn = lambda n:2*n
iterator = Make_iterator(fn)

for i in range(4):     
    print("iterator",iterator())
print('==========================')   
for i in range(2,4):     
    print("iterator", iterator())
print('==========================') 
it = Make_iterator(fn)
for i in range(2):
    print("it" ,it())
 
print('==========================')   
for i in range(2,4):     
    print("iterator",iterator())
