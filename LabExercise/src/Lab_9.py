class Account(object):
        
        interest =0.3
        def __init__(self, account_holder):
            self.balance = 0
            self.holder = account_holder
        def deposit(self, amount):
            self.balance = self.balance + amount
            return self.balance
        def withdraw(self, amount):
            if amount > self.balance:
                return 'Insufficient funds'
            self.balance = self.balance - amount
            return self.balance

tom_account = Account('Tom')
bor_account=Account('Bor')
print(tom_account.deposit(100))
print(tom_account.withdraw(90))
print(tom_account.withdraw(90))
tom_account.interest=0.2
print(tom_account.interest)
print(bor_account.interest)
print(Account.mro())


# ----------------- Class ------------------------
class Class1(object):
    def __init__(self, n1=0, n2=0, str1='None'):
        self.num1 = n1
        self.num2 = n2
        self.str = str1
    def printC(self):
        print(self.num1, self.num2, self.str)
# ------------------------------------------------
#t1 = Class1(2,3)
#t1.printC()    # => 2 3 None
#t2=t1
#t2.printC()    # => 2 3 None
#t1.str = 'Test'
#t1.printC()    # => 2 3 Test
#t2.printC()    # => 2 3 Test
# ------------------------------------------------
#t1 = Class1(2,3)
#t3 = copy.copy(t1)
#t3.printC()    # => 2 3 None
#t1.str = 'Test'
#t1.printC()    # => 2 3 Test
#t3.printC()    # => 2 3 None


# ------------ Class Attributes ------------------
#hasattr(t1,'num2') # => True
#hasattr(t1,'num3') # => False
#t1.__dict__        # => {'num1': 2, 'str': 'Test', 'num2': 3}

#for attr in t1.__dict__:
#    print( attr,getattr(t1,attr))    
#num1 2
#str Test
#num2 3


### Original Point classes
class Point:
    color = 'blue'

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def str(self):
        return '(x=%d, y=%d)' % (self.x, self.y)

    def prt(self):
        print(self.str())

    def shift(self, number):
        self.x += number
        self.y += number

    def eq(self, other):
        return self.x == other.x  and  self.y == other.y

class ColorPoint(Point):
    color = 'red'

    def str(self):
        return Point.str(self) + ' [color = %s]' % self.color

#p = Point(1, 2)
#q = ColorPoint(3, 4)
#q2 = ColorPoint(5, 6)
#p.prt()
#q.prt()
#p.shift(3)
#p.prt()
#print(q.eq(q))
#q.color = 'green'
#q.prt()
#q2.prt()
