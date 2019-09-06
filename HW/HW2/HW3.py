# task 1 -------------------------------------------------- task1
print(" task 1 -------------------------------------------------- task 1")

def make_date(year,month,day):
    def dispatch(massege):
        if massege == 'year':
            return year
        if massege == 'month':
            return month
        if massege == 'day':
            return day
        return 'error'
    return dispatch
#-----------------------------------
#d = make_date(2016,12,26)
#print(d)
#print(type(d))
#print(d('year'))
#-----------------------------------
#level 1 - user api
def year(d):# func get
    return d('year')
def month(d):# func get
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    x=d('month')
    return months[x-1]
def str_date(d):
    string = ""+str(day(d))+'th of '+month(d)+', ' + str(year(d))
    return string
def day(d):# func get
    return d('day')


#str_date(d)
#print(str_date(d))
#s = make_date(2018,12,26)
#print(s)
#print(str_date(s))
d = make_date(2016, 12, 26)
print(d)
#function make_date.<locals>.dispatch at 0x02A880C0>
print(year (d))
#2016
print(month (d))
#December
print(day (d))
#26
print(str_date(d))


# task 2 -------------------------------------------------- task2
print(" task 2 -------------------------------------------------- task 2")


data = "/Users/someuser/file.py;/tmp/download/file.zip;/tmp/download/file2.zip; /;/usr/local/bin;/User/someuser/file..py;/tmp/file."
def  data_preprocessing_tree(data):
   
    # a ---> enumerate
    enumerate = data.split(';')
    #print(enumerate)
    # b ---> clean (noise removal)
    clean=filter(lambda x: '..' not in x and '//' not in x, enumerate)
    #print(clean)
    # c ---> complete missing values
    completeMissingValues = set(map(lambda x: str(x + 'txt') if x[-1:] == '.' else str(x), clean))
    #print(completeMissingValues)
    # d ---> accumulate i ---> build tree
    #set(filter(lambda elem :"." in elem , set(map(lambda x: str(x + 'txt') if x[-1:] == '.' else str(x), filter(lambda x: '..' not in x and '//' not in x, data.split(';'))))))
    #files = set(filter(lambda elem :"." in elem , completeMissingValues))
    #print(files)
    return completeMissingValues
 
def data_preprocessing_file_types(data):
    # a ---> enumerate
    enumerate = data.split(';')
    #print(enumerate)
    # b ---> clean (noise removal)
    clean=filter(lambda x: '..' not in x and '//' not in x, enumerate)
    #print(clean)
    # c ---> complete missing values
    completeMissingValues = set(map(lambda x: str(x + 'txt') if x[-1:] == '.' else str(x), clean))
    x = set(filter(lambda x : '.' in x,completeMissingValues))
    return x

print("data_preprocessing_tree ERROR ---> task is not yet complete")
print(data_preprocessing_tree(data))
print("data_preprocessing_file_types ERROR ---> task is not yet complete")
print(data_preprocessing_file_types(data))

# task 3 -------------------------------------------------- task 3
print(" task 3 -------------------------------------------------- task 3")

def make_currency(amount,symbol):
    # a
    # message passing method.
    def get_value(massage):
        if massage == 'amount':
            return amount
        if massage == 'symbol':
            return symbol
        return 'Error'
    # b
    # message passing method.
    def set_value(massage,change):
        nonlocal amount, symbol
        if massage == 'amount':
            amount = change
        if massage == 'symbol':
            symbol = change
        return 'Error'
    #print(amount)
    # c
    def str_it():
        print("{0}{1:.2f}".format(symbol, amount))
    # d   
    def convert(lam,s):
        nonlocal amount, symbol
        symbol = s
        amount = lam(amount)
        
    def dispatch(massage):
        if massage == "get_value":
            return get_value
        elif massage == "set_value":
            return set_value
        elif massage == "str":
            return str_it
        elif massage == "convert":
            return convert
        return 'Error'
    return dispatch 

c = make_currency(10.50, '$')
print(c('get_value')('amount'))
print(c('get_value')('symbol'))
c('set_value')('amount', 50)
print(c('get_value')('amount'))
c('str')()
c('convert')(lambda x: x*3.87, 'NIS') 
c('str')()


# task 4 -------------------------------------------------- task 4
print(" task 4 -------------------------------------------------- task 4")

def get_reverse_map_iterator(s, g=lambda x: x):
    i = len(s)-1
    # a
    def next():
        nonlocal i
        if has_more():
            i -=1
            #print("index in fun next",i)
            return g(s[i+1])
        else:
            return "no more items"
    # b
    def has_more():
        
        if i != -1:
            #print("index in fun has_more",i)
            return True
        else:
            return False

    dispatch = {"next": next, "has_more": has_more}
    
    return dispatch

it = get_reverse_map_iterator((1,3,6), lambda x: 1/x)
while it['has_more']():
    print(it['next']())
it = get_reverse_map_iterator((1,3,6))
for _ in range(1,6):
    print(it['next']())


# task 5 -------------------------------------------------- task 5
print(" task 5 -------------------------------------------------- task 5")
empty_rlist = None
#===================================#

def make_rlist(first, rest):
    return(first,rest)
#===================================#

def rest(node):
    return node[1]
#===================================#

def first(node):
    return node[0]
#===================================#

def len_rlist(node):
        i=0
        while node!=empty_rlist:
            i=i+1
            node = rest(node)
        return i
#===================================#

def getitem_rlist(s, count):
    while count > 0:
        s = rest(s)
        count = count - 1
    return first(s)

#===================================#
#===================================#
#===================================#

def make_mutable_rlist(rlist = empty_rlist):
    def copyctor(other_rlist):
        
        newRlist = empty_rlist
        if (other_rlist != None):
            leng= other_rlist["length"]()-1
            while leng>=0:
                newRlist = make_rlist(other_rlist['get_item'](leng), newRlist)
                leng-=1
        return newRlist
    
    contents = copyctor(rlist)
#===================================#  
    def length():
        return len_rlist(contents)
#===================================#
        
    def get_item(ind):
        return getitem_rlist(contents, ind)
#===================================#
    def push_first(value):
        nonlocal contents
        contents = make_rlist(value, contents)
#===================================#
    def pop_first():
        nonlocal contents
        
        temp = first(contents)
        contents= rest(contents)
        return temp   
#===================================#
    def strr():
        string='['
        t=contents
        while t!=empty_rlist:
            temp=first(t)
            t=rest(t)
            string+='{0}'.format(temp)
            if t!=None:
                string+=','
        string+=']'
        return string
#===================================#
        
    def get_iterator():
        index=0
        def hasNext():
            if index==length():
                return False
            return True
        def next():
            nonlocal index
            index+=1
            if index-1<length():
                return get_item(index-1)
        return{'hasNext':hasNext,'next':next}
#===================================#
    def slice(start, end):
        newS =  make_mutable_rlist()
        for i in range(len_rlist(contents)):
            if start<=i<end:
                newS["push_first"](getitem_rlist(contents, i))
        
        return newS
#===================================#
       
    def extend(mrlist):
        
        
        nonlocal contents
        leng, temp = mrlist["length"](), empty_rlist
        for i in range(leng-1, -1, -1):
            temp = make_rlist(mrlist['get_item'](i), temp)
        leng = len_rlist(contents)
        for i in range(leng-1, -1, -1):
            temp = make_rlist(getitem_rlist(contents, i), temp)
        contents = temp
        
        '''
        temp = make_mutable_rlist()
        for i in range( len_rlist(contents)):#1,2,3 to temp
            #print(type(temp), type(contents))
            temp['push_first']( contents[0] )
            contents = contents[1]
        for i in range( temp['length']() ):
            lst["push_first"](temp['pop_first']() ) 
        '''
        
    #dispatch = { }   
    return {'length':length, 'get_item':get_item, 'push_first':push_first, 'pop_first': pop_first, 'str': strr, 'get_iterator': get_iterator, 'slice': slice, 'extend': extend}


my_list = make_mutable_rlist() 
for x in range(4):
    my_list['push_first'](x) 
print(my_list['str']()) #+
ext = make_mutable_rlist(my_list)
my_list['extend'](ext)
print(my_list['str']())
print(my_list['slice'](0,2)['str']())
your_list = make_mutable_rlist(my_list)
print(your_list['str']())
it = my_list['get_iterator']() 
while it['hasNext']():
    print(it['next']())


