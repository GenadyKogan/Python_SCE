
from functools import reduce
'''task 1'''
#-----------------------------------#
def make_time(hour,minute,second):
    ''' doc tar 1'''
    def dispatch(message):
        if message == 'hour':
            return hour
        if message == 'minute':
            return minute
        if message == 'second':
            return second
    return dispatch
#-----------------------------------#
def getitem_date(p,i):
    return p(i)
#-----------------------------------#
def hour(d):#function get
    return getitem_date(d,'hour')
#-----------------------------------#
def minute(d):
    return getitem_date(d,'minute')
#-----------------------------------#
def second(d):
    return getitem_date(d,'second')
#def second(d):
    #return d('second') 
#-----------------------------------#

def print_time(date,message = None):
        if message == None:
            print('{0:0=2d}:{1:0=2d}:{2:0=2d}'.format(hour(date),minute(date),second(date)))
            return
        elif message == 'HH:MM:SS':
            hour_temp = hour(date)
            if hour(date) == 0:
                hour_temp = 12
            elif hour(date) >12:
                hour_temp = hour_temp -12
            print('{0:0=1d}:{1:0=2d}:{2:0=2d} {3}'.format(hour_temp,minute(date),second(date),('A.M.' if  0 <= hour(date) < 12 else 'P.M')))
            return 
        elif message == 'HH:MM':
            if hour(date) > 12:
                hour_temp =  hour(date) 
                hour_temp = hour_temp -12
                print('{0:0=1d}:{1:0=2d} {2}'.format(hour_temp,minute(date),('A.M.' if  0 <= hour(date) <= 12 else 'P.M')))
            if hour(date) == 0:
                print('{0:0=1d}:{1:0=2d} {2}'.format(hour(date)+12,minute(date),('A.M.' if  0 <= hour(date) <= 12 else 'P.M')))
        elif message =='HH':
            print('{0:0=1d} {1}'.format(hour(date),('A.M.' if  0 <= hour(date) <= 12 else 'P.M')))
            return 
#-----------------------------------#
def time_difference(t1,t2):
    temp_hour = hour(t1) - hour(t2)
    temp_minute = minute(t1) - minute(t2)
    temp_second = second(t1) - second(t2)
    if temp_minute < 0:
        temp_minute = temp_minute + 60
        if temp_hour==0:
            temp_hour = 23
        else:
            temp_hour = temp_hour - 1
    if temp_second < 0:
        temp_second = temp_second+60
        temp_minute = temp_minute-1
    temp_hour = abs(temp_hour)
    return  make_time(temp_hour, temp_minute, temp_second)
#-----------------------------------#        
def time_correction(t1,sec):
    temp_sec = abs(sec)
    secondsInHour = 60 * 60
    secondsInMinute = 60
    #1
    hours = (temp_sec//secondsInHour)
    remainingSeconds = temp_sec - (hours * secondsInHour)
    #2
    minutes = remainingSeconds//secondsInMinute
    remainingSeconds = remainingSeconds - (minutes*secondsInMinute)
    #3
    seconds = remainingSeconds
    if sec>0:
        return make_time(hour(t1) + hours,minute(t1) + minutes,second(t1) + seconds)
    if sec<=0:
        t2 = make_time(hours, minutes, seconds)
        
        return time_difference(t1,t2)   
#-----------------------------------# 
def driver_task1():  
    help(make_time)
    t1 = make_time(11,5,47)
    t3 = make_time(11,5,47)
    print(t1)
    print(hour(t1))
    print(minute(t1))
    print_time(t1)
    t2 = make_time(0, 12, 23)
    print_time(t2,'HH:MM')
    print_time(time_difference(t1, t2))
    print_time(time_correction(t1, 4623),'HH:MM:SS')
    t2 = time_correction(t2, -920)
    print_time(t2)
    print_time(t2,'HH:MM')
driver_task1()
#-----------------------------------#     


'''task 2'''
#-----------------------------------# 
def make_tree(value,left,right):
    ''' doc tar 2'''
    def dispatch(message):
        if message == 'value':
            return value
        if message == 'right_node':
            return right
        if message == 'left_node':
            return left
    return dispatch
#-----------------------------------# 
def getitem_node(f,i):
    return f(i)
#-----------------------------------# 
def right(node):
    return getitem_node(node, 'right_node')
#-----------------------------------#
def left(node):
    return  getitem_node(node,'left_node')
#-----------------------------------#
def value(node):
    #return getitem_node(node, 'value')
    return node("value")
#-----------------------------------#
def mirror_tree(tree):
    if tree:
        return make_tree(value(tree), mirror_tree(right(tree)), mirror_tree(left(tree)))
#-----------------------------------#
def print_tree(tree):
    if tree!=None:
        print_tree(left(tree))
        print(value(tree),end=" ")
        print_tree(right(tree)) 
#-----------------------------------#        
def min_val(tree): 
    res = value(tree)
    if tree:  
        if left(tree) != None:
            lres = min_val(left(tree))
            if lres<res:
                res = lres
        if right(tree) != None:    
            rres = min_val(right(tree))
            if rres<res:
                res = rres       
    return res
#-----------------------------------#

def driver_task2():
    help(make_tree)
    tree = make_tree(12,make_tree(6,make_tree(8,None,None),None),make_tree(7,make_tree(2,None,None),make_tree(15,None,None)))
    print(tree)
    print(value(tree))
    print(value(left(tree)))
    print(left(right(tree)))
    print(value(left(right(tree))))
    print_tree(tree)
    print()
    tree1 = mirror_tree(tree)
    print_tree(tree1)
driver_task2()
 
'''task 3'''
"""
data=(20,-45,133,8,400,7,-300,68)
func=(lambda x: x>0,lambda x: x%2==0,lambda x: 9<abs(x)<100)
foo=list(reduce(lambda x,y: x+y,list((list(filter(func[i] ,data)) for i in range(len(func)) ))))
print (foo)
"""
#print((lambda func,data:tuple(filter(lambda x: True if list(reduce(lambda x,y: x+y,list((list(filter(func[i] ,data)) for i in range(len(func)) )))).count(x)==1 else False,reduce(lambda x,y: x+y,list((list(filter(func[i] ,data)) for i in range(len(func)) )))))          )((lambda x: x>0,lambda x: x%2==0,lambda x: 9<abs(x)<100),(20,-45,133,8,400,7,-300,68)))

'''task 4'''
def sets(mySeq):
    ''' doc tar 4'''
#=============================== a
    seq = mySeq
    setGroup = []
    for x in range(1,21):
        setGroup.append(x)
    myGroup = tuple(setGroup)
    
    likefilter = []
    for x in seq:
        if x<= 20 and x >= 0:
            likefilter+=[x]
        seq= tuple(likefilter)  
    
#=============================== b    
    def view ():
        st=''
        for x in seq:
            st += str(x) + ', '
        st = st[:-2]  
        #print(st) 
        return "{0}{1}{2}".format('{',st,'}')
#=============================== c
    def inSeq(value):
        if value in seq:
            return True
        return False 
        #return value in seq  
#=============================== d
    def notInSeq(value):
        return value not in seq
#=============================== e
    def complement():
        temp = []
        for x in range(1,21):
            if x not in seq:
                temp.append(x)
        seq2 = tuple(temp)
        #print(seq2)
        return sets(seq2)
#===============================  
    def newSeq(new_seq):
        nonlocal seq
        seq= new_seq
        return sets(seq)
#=============================== f
    def andOperation(seq2):
        nonlocal seq
        seq = list(seq)
        for i in myGroup:
            if seq2('in', i) and i not in seq:
                seq.append(i)
                #seq += (i,)
        seq = tuple(seq)        
        return sets(seq)
#=============================== g        
    def starOperation(seq2):
        starSeq = []
        for i in myGroup:
            if seq2('in',i) and i in seq:
                starSeq.append(i)
        starSeq = tuple(starSeq)
        return sets(starSeq)    
#=============================== h 
    def divideOperation(seq2):
        starSeq = []
        for i in myGroup:
            if seq2('not in',i) and i in seq:
                starSeq.append(i)
        starSeq = tuple(starSeq)
        return sets(starSeq)
#=============================== i
    def xorOperation(seq2):
        temp = ()
        for i in myGroup:
            if seq2('in',i) and i not in seq or seq2('not in',i) and i in seq :
                temp += (i,)
        return sets(temp)
#===============================        
    def dispatch(message,args=None):
        if message == 'view':
            return view()
        if message == 'in':
            return inSeq(args)
        if message == 'not in':
            return notInSeq(args)
        if message == 'not':
            return complement()
        if message == 'set':
            return newSeq(args)
        if message == '+':
            return andOperation(args)
        if message == '*':
            return starOperation(args)
        if message == '\\':
            return divideOperation(args)
        if message == 'xor':
            return xorOperation(args)
        
    return dispatch  



def driver_task4():
    
    help(sets)
    s1 = sets((1,2,3,4,5,100)) 
    print(s1)   
    s1('view') 
    print(s1('in',3))
    print(s1('not in',31))
    print(s1('not in',3))
    s2 = s1('not')
    s1('set',(1,2,3,4,5,7,9,12,17))
    s2('set',(2,4,5,10,14,16,20)) 
    print(s1('+',s2)('not')('view'))
    print(s1('*',s2)('xor',s1('\\',sets((2,3,5,12))))('view') )
    
driver_task4()

#--------------------------------------#
'''task 5'''
    
def matrix(matr,lin,colum):
    '''doc tar5'''
    mat=[]
    mat=list(matr) 

    def add_Line(num):
        nonlocal lin,mat
        mat.extend(num)
        lin+=1
        return mat
    #
    def add_column(num):
        nonlocal colum,mat
        col=1
        for k in num:
            mat.insert(colum*col+col-1,k)
            col+=1
        colum+=1
        return mat
     #  
    def Print():
        index=-1
        def Print():
            def Print():  
                nonlocal index
                index+=1
                ind=(index%(colum*lin))
                return mat[ind]
            return {'Print':Print} 
        return {'Print':Print}
    #
    def  line():
        return lin
    #
    def column():
        return colum
    #
    def shift_up():
        nonlocal mat
        index=(-lin+1)*colum
        nMat=mat[index::]
        nMat.extend(mat[:colum])
        mat=nMat
        return mat
    #
    def shift_down():
        nonlocal mat
        index=colum+colum
        nMat=[]
        nMat=mat[index::]
        nMat.extend(mat[0:index:1])
        mat=nMat
        return mat
    #
    def shift_right():
        nonlocal mat
        nMat=[]
        col=0
        for i,elm in enumerate(mat,0):
            if (i+1)% colum!=0:
                nMat.append(elm)
            if (i+1)% colum==0:
                nMat.insert(col,elm)
                col+=colum
        mat=nMat
        return mat
     #
    def shift_left():
        nonlocal mat
        nMat=[]
        col=colum-1
        for i,elm in enumerate(mat,0):
            if i% colum!=0:
                nMat.append(elm)
        for i,elm in enumerate(mat,0):
            if i% colum==0:
                nMat.insert(col,elm)
                col+=colum
        
        mat=nMat
        return mat
    #  
    def transpose():
        nonlocal mat,colum,lin
        nMat=[]
        k=0
        for i,elm in enumerate(mat,0):
            if i% colum==k:
                nMat.append(elm)        
        for i,elm in enumerate(mat,0):
            if i% colum==k+1:
                nMat.append(elm) 
        for i,elm in enumerate(mat,0):
            if i% colum==k+2:
                nMat.append(elm) 
        for i,elm in enumerate(mat,0):
            if i% colum==k+3:
                nMat.append(elm) 
        for i,elm in enumerate(mat,0):
            if i% colum==k+4:
                nMat.append(elm) 
                 
        colum=3
        lin=5
        mat=nMat
        return mat
    
    return {'add_Line':add_Line,'add_column':add_column,'Print':Print, 'line': line, 'column':column, 'shift_up':shift_up,'shift_down':shift_down, 'shift_right':shift_right,'shift_left':shift_left,'transpose':transpose}


help(matrix)      
m=matrix((1,2,3,4,5,6,7,8),2,4)
print(m['add_Line']((1,3,5,7)))
print(m['add_column']((2,4,6))) 

matrix=m['Print']() 
for i in range(m['line']()):  
    line=matrix['Print']()  
    for i in range(m['column']()):   
        print(line['Print'](),end=' ')  
    print() 
print(m['shift_up']())
print(m['shift_right']())
print(m['transpose']())
  
matrix=m['Print']() 
for i in range(m['line']()):  
    line=matrix['Print']()  
    for i in range(m['column']()):   
        print(line['Print'](),end=' ')  
    print() 
