# ===================== Task 1A =====================
# ==========================================
from asyncio.subprocess import DEVNULL
class UndergraduateStudent(object):
    '''class for undergraduate students'''
    # ++++++++++++++++++++++++++++++++++++++
    def __init__(self, _name, _dept, _year):
        '''The function enters values to the class fields'''
        self.name = _name
        self.dept = _dept
        self.year = _year
        self._DegreName = 'first'
        self._Dname = None

    # ++++++++++++++++++++++++++++++++++++++
    def AdMatai(self):
        '''The function calculates the number of years left to complete the degree'''
        self.x = 5 - self.year
        return self.x

    # +++++++++++++++++++++++++++++++++++++++
    def Introduce(self):
        '''The function Prints the text of the student's presentation, including the details:
                degree, department, name, and number of years left to complete the degree:'''
        if self._Dname == None:
            print("I am a student for the", self._DegreName, "degree in", self.dept, 'department, my name is',
                  self.name, 'and I will finish my studies in', self.AdMatai(), 'years')
        else:
            print("I am a student for the", self._DegreName, "degree in", self.dept, 'department, my name is',
                  self._Dname,
                  self.name, 'and I will finish my studies in', self.AdMatai(), 'years')

    # +++++++++++++++++++++++++++++++++++++++
    def __repr__(self):
        '''The function  Which returns a text representation of the performance to be presented by the interpreter:
               the name of a class And attribute values (including functions).'''
        return 'UndergraduateStudent("%s","%s",%d)' % (self.name, self.dept, self.year)

    # +++++++++++++++++++++++++++++++++++++++
    def __str__(self):
        '''The function Prints the student's name, title, and department'''
        return '{0} {1} {2} {3} {4}'.format("MSc student", self.name, "from", self.dept, "department")


# ==========================================
class GraduateStudent(UndergraduateStudent):
    '''class for graduate students'''
    # ++++++++++++++++++++++++++++++++++++++
    def __init__(self, _name=0, _dept=0, _year=0):
        '''The function enters values to the class fields'''
        UndergraduateStudent.__init__(self, _name, _dept, _year)
        self._DegreName = 'Master'
        self._Dname = 'Bachelor'

    # ++++++++++++++++++++++++++++++++++++++
    def AdMatai(self):
        '''The function calculates the number of years left to complete the degree'''
        self.x = 4 - self.year
        return self.x

    # ++++++++++++++++++++++++++++++++++++++
    def Introduce(self):
        UndergraduateStudent.Introduce(self)

    # ++++++++++++++++++++++++++++++++++++++
    def __repr__(self):
        return UndergraduateStudent.__repr__(self)

    # ++++++++++++++++++++++++++++++++++++++
    def __str__(self):
        return UndergraduateStudent.__str__(self)


# ==========================================
class PhDStudent(UndergraduateStudent):
    '''class for PhD students'''
    # ++++++++++++++++++++++++++++++++++++++
    def __init__(self, _name=0, _dept=0, _year=0):
        '''The function enters values to the class fields'''
        UndergraduateStudent.__init__(self, _name, _dept, _year)
        self._DegreName = 'Ph.D.'
        self._Dname = 'Almost Doctor'

    # ++++++++++++++++++++++++++++++++++++++
    def AdMatai(self):
        '''The function calculates the number of years left to complete the degree'''
        self.x = 3 - self.year
        return self.x

    # ++++++++++++++++++++++++++++++++++++++
    def Introduce(self):
        UndergraduateStudent.Introduce(self)

    # ++++++++++++++++++++++++++++++++++++++
    def __repr__(self):
        return UndergraduateStudent.__repr__(self)

    # ++++++++++++++++++++++++++++++++++++++
    def __str__(self):
        return UndergraduateStudent.__str__(self)

# --------------------------------EXCEPTION------------------------------------------#
class NegativeNumberError(Exception):
    '''class exception'''
    def __init__(self):
        Exception.__init__(self, "Negative number")

def exception(x, y, z):
    try:
        if type(x) is not str or type(y) is not str or type(z) is not int:
            raise ValueError('Not Right Type')
    except ValueError:
        print('Value Error')
        return 1
    else:
        print('No Error')
    finally:
        print('End')

# ==========================================
def DriverTask1():
    try:
        ##check type
        assert exception("Moshe", "SE", 3) != 1
    except AssertionError:
        sys.exit()
    else:
        us = UndergraduateStudent("Moshe", "SE", 3)
        us.Introduce()
        print()
    try:
        ##check type
        assert exception("Asaf", "CS", 2) != 1
    except AssertionError:
        sys.exit()
    else:
        ms = GraduateStudent("Asaf", "CS", 2)
        ms.Introduce()
        print()
    print(eval(repr(ms)))

    try:
        ##check type
        assert exception("Eli", "ISE", 1) != 1
    except AssertionError:
        sys.exit()
    else:
        print()
        ps = PhDStudent("Eli", "ISE", 1)
        ps.Introduce()


#DriverTask1()

# ===================== Task 1C - Shmython =====================

# ==========================================
def make_class(attrs, base=None):
    """Return a new class (a dispatch dictionary) with given class attributes"""

    # print(attrs)
    def get(name):
        ''' Getter: class attribute (looks in this class, then base)'''
        if name in attrs:
            return attrs[name]
        elif base:
            return base['get'](name)


    def set(name, value):
        '''Setter: class attribute (always sets in this class)'''
        attrs[name] = value

    # Return a new initialized objec'aaa': 5.5t instance (a dispatch dictionary)
    def new(*args):
        # instance attributes (hides encapsulating function's attrs)
        attrs = {}

        # Getter: instance attribute (looks in object, then class (binds self if callable))
        def get(name):
            if name in attrs:
                return attrs[name]
            else:
                value = cls['get'](name)
                if callable(value):
                    return lambda *args: value(obj, *args)
                else:
                    return value

        # Setter: instance attribute (always sets in object)
        def set(name, value):
            attrs[name] = value

        # instance dictionary
        obj = {'get': get, 'set': set}

        # calls constructor if present
        init = get('__init__')
        if init: init(*args)

        return obj

    # class dictionary
    cls = {'get': get, 'set': set, 'new': new}
    return cls


# ==========================================
def Make_UndergraduateStudent_Class():
    '''shmayton undergraduate students'''
    def __init__(self, _name, _dept, _year, _DegreName=None):
        self['set']('name', _name)
        self['set']('dept', _dept)
        self['set']('year', _year)
        self['set']('_DegreName', 'first')

    # +++++++++++++++++++++++++++++++++++++++
    def AdMatai(self):
        return 5 - self['get']('year')

    # ++++++++++++++++++++++++++++++++++++++
    def introduce(self):
        print("I am a student for the", self['get']('_DegreName'), "degree in", self['get']('dept'),
              'department, my name is',
              self['get']('name'), 'and I will finish my studies in', AdMatai(self), 'years')

    # ++++++++++++++++++++++++++++++++++++++
    def __str__(self):
        return '{0} {1} {2} {3} {4}'.format("MSc student", self['get']('name'), "from", self['get']('dept'),
                                            "department")

    # ++++++++++++++++++++++++++++++++++++++
    return make_class(locals())


# ==========================================
def Make_GraduateStudent_Class():
    '''shmayton graduate students'''
    def AdMatai(self):
        return 4 - self['get']('year')

    # ++++++++++++++++++++++++++++++++++++++
    def introduce(self):
        print("I am a student for the Master degree in", self['get']('dept'), 'department, my name is Bachelor',
              self['get']('name'), 'and I will finish my studies in', AdMatai(self), 'years')

    # ++++++++++++++++++++++++++++++++++++++
    return make_class(locals(), Make_UndergraduateStudent_Class())


# ==========================================
def Make_PhDStudent_Class():
    '''shmayton PhD students'''
    def AdMatai(self):
        return 3 - self['get']('year')

    # ++++++++++++++++++++++++++++++++++++++
    def introduce(self):
        print("I am a student for the Ph.D. degree in", self['get']('dept'), 'department, my name is Almost Doctor',
              self['get']('name'), 'and I will finish my studies in', AdMatai(self), 'years')
        # ++++++++++++++++++++++++++++++++++++++

    return make_class(locals(), Make_UndergraduateStudent_Class())


# ==========================================
def DriverTask1B():
    UndergraduateStudent = Make_UndergraduateStudent_Class()
    us = UndergraduateStudent['new']("Moshe", "SE", 3)
    us['get']('introduce')()
    print(us['get']('__str__')())
    GraduateStudent = Make_GraduateStudent_Class()
    ms = GraduateStudent['new']("Asaf", "CE", 2)
    ms['get']('introduce')()
    print(ms['get']('__str__')())
    PhDStudent = Make_PhDStudent_Class()
    ps = PhDStudent['new']("Eli", "ISE", 1)
    ps['get']('introduce')()
    print(ps['get']('__str__')())


#DriverTask1B()

# ===================== Task 2A =====================

convertion = {('min', 'hour'): 60, ('hour', 'day'): 24, ('day', 'week'): 7}


def add(x1, x2):
    return x1.amount() + x2.amount()


def sub(x1, x2):
    return x1.amount() - x2.amount()


# ==========================================
class Hour(object):
    # ++++++++++++++++++++++++++++++++++++++
    def __init__(self, value):
        self.value = value

    # ++++++++++++++++++++++++++++++++++++++

    def amount(self):
        return self.value * convertion[('min', 'hour')]

    # ++++++++++++++++++++++++++++++++++++++
    def __add__(self, other):
        return self.value + other.value

    # ++++++++++++++++++++++++++++++++++++++
    def __str__(self):
        return '{0} {1}'.format(self.value, 'hour')

    # ++++++++++++++++++++++++++++++++++++++
    def __repr__(self):
        # return "{Class}({Hour})".format(Class = self.__class__.__name__ ,  Hour = self.time)
        return "Hour({0})".format(self.value)


# ==========================================
class Day(object):
    # ++++++++++++++++++++++++++++++++++++++
    def __init__(self, value):
        self.value = value

    # ++++++++++++++++++++++++++++++++++++++
    def amount(self):
        return self.value * convertion[('min', 'hour')] * convertion[('hour', 'day')]

    # ++++++++++++++++++++++++++++++++++++++
    def __add__(self, other):
        return self.value + other.value

    # ++++++++++++++++++++++++++++++++++++++
    def __str__(self):
        return '{0} {1}'.format(self.value, 'day')

    # ++++++++++++++++++++++++++++++++++++++
    def __repr__(self):
        return "Day({0})".format(self.value)
    # ==========================================


class Week(object):
    # ++++++++++++++++++++++++++++++++++++++
    def __init__(self, value):
        self.value = value

    # ++++++++++++++++++++++++++++++++++++++
    def amount(self):
        return self.value * convertion[('min', 'hour')] * convertion[('hour', 'day')] * convertion[('day', 'week')]

    # ++++++++++++++++++++++++++++++++++++++
    def __add__(self, other):
        return self.value + other.value

    # ++++++++++++++++++++++++++++++++++++++
    def __str__(self):
        return '{0} {1}'.format(self.value, 'week')

    # ++++++++++++++++++++++++++++++++++++++
    def __repr__(self):
        return "Week({0})".format(self.value)
    # ==========================================


def DriverTask2A():
    s = Day(5)
    # s.amount()
    d = Week(2)
    print(d.amount())
    e = Hour(50)
    print(e.amount())
    print(d + s)
    print(add(e, d))
    z = eval(repr(d))
    print(z)
    print(s)


#DriverTask2A()

# ===================== Task 2B =====================

def type_tag(x):
    return type_tag_tags[type(x)]


type_tag_tags = {Hour: 'hour', Day: 'day', Week: 'week'}


# ==========================================
# ====== sum
# ====== hour
def AddHour(x, y):
    return "Hour({0})".format(((add(x, y)) // convertion[('min', 'hour')]))


def AddHourDay(x, y):
    return "Hour({0})".format(((add(x, y)) // convertion[('min', 'hour')]))


def AddHourWeek(x, y):
    return "Hour({0})".format(((add(x, y)) // convertion[('min', 'hour')]))


# ====== day
def AddDay(x, y):
    return "Day({0})".format(((add(x, y)) // convertion[('min', 'hour')] // convertion[('hour', 'day')]))


def AddDayWeek(x, y):
    return "Day({0})".format(((add(x, y)) // convertion[('min', 'hour')] // convertion[('hour', 'day')]))


# ====== week
def AddWeek(x, y):
    return "Week({0})".format(
        ((add(x, y)) // convertion[('min', 'hour')] // convertion[('hour', 'day')] // convertion[('day', 'week')]))


# ====== sub
def SubHour(x, y):
    return "Hour({0})".format(((sub(x, y)) // convertion[('min', 'hour')]))


def SubHourDay(x, y):
    return "Hour({0})".format(((sub(x, y)) // convertion[('min', 'hour')]))


def SubHourWeek(x, y):
    return "Hour({0})".format(((sub(x, y)) // convertion[('min', 'hour')]))


# ====== day
def SubDay(x, y):
    return "Day({0})".format(((sub(x, y)) // convertion[('min', 'hour')] // convertion[('hour', 'day')]))


def SubDayHour(x, y):
    return "Hour({0})".format(((sub(x, y)) // convertion[('min', 'hour')]))


def SubDayWeek(x, y):
    return "Day({0})".format(((sub(x, y)) // convertion[('min', 'hour')] // convertion[('hour', 'day')]))


# ====== week
def SubWeek(x, y):
    return "Week({0})".format(
        ((sub(x, y)) // convertion[('min', 'hour')] // convertion[('hour', 'day')] // convertion[('day', 'week')]))


def SubWeekHour(x, y):
    return "Hour({0})".format(((sub(x, y)) // convertion[('min', 'hour')]))


def SubWeekDay(x, y):
    return "Day({0})".format(((sub(x, y)) // convertion[('min', 'hour')] // convertion[('hour', 'day')]))


# ==========================================
def apply(operator_name, x, y):
    '''A generic function that performs the addition and subtraction operations between different types
        and returns a result as a representation of a class that represents the "smaller" type.'''
    types = (type_tag(x), type_tag(y))
    key = (operator_name, types)
    return apply.implementations[key](x, y)


apply.implementations = {  # ===== sum
    ('add', ('hour', 'hour')): AddHour,
    ('add', ('hour', 'day')): AddHourDay,
    ('add', ('hour', 'week')): AddHourWeek,
    ('add', ('day', 'day')): AddDay,
    ('add', ('day', 'hour')): lambda x, y: AddHourDay(y, x),
    ('add', ('day', 'week')): AddDayWeek,
    ('add', ('week', 'week')): AddWeek,
    ('add', ('week', 'hour')): lambda x, y: AddHourWeek(y, x),
    ('add', ('week', 'day')): lambda x, y: AddDayWeek(y, x),
    # ===== sub
    ('sub', ('hour', 'hour')): SubHour,
    ('sub', ('hour', 'day')): SubHourDay,
    ('sub', ('hour', 'week')): SubHourWeek,
    ('sub', ('day', 'day')): SubDay,
    ('sub', ('day', 'hour')): SubDayHour,
    ('sub', ('day', 'week')): SubDayWeek,
    ('sub', ('week', 'week')): SubWeek,
    ('sub', ('week', 'hour')): SubWeekHour,
    ('sub', ('week', 'day')): SubWeekDay}


def DriverTask2B():
    print(apply('add', Week(1), Day(1)))
    # print(apply('add', Day(50), Week(3)))
    print(apply('sub', Week(1), Day(1)))


#DriverTask2B()


# ===================== Task 2C =====================
# convertion = {('min','hour'):60,('hour','day'):24,('day','week'):7}


def DayToHour(a, b=None):
    '''Generic function that performs the action after conversion of time to hours.'''
    new = Hour(0)

    if (type(a).__name__ == 'Day'):
        new.value = a.value * convertion[('hour', 'day')]
    elif (type(b).__name__ == 'Day'):
        new.value = b.value * convertion[('hour', 'day')]

    return new  # 'Hour({})'.format(new.value)


def WeekToDay(a, b=None):
    new = Day(0)
    if (type(a).__name__ == 'Week'):
        new.value = a.value * convertion[('day', 'week')]
    elif (type(b).__name__ == 'Week'):
        new.value = b.value * convertion[('day', 'week')]
    return new  # 'Day({})'.format(new.value)


def WeekToHour(a, b=None):
    new = Day(0)
    if (type(a).__name__ == 'Week'):
        new.value = a.value * convertion[('day', 'week')] * convertion[('hour', 'day')]
    elif (type(b).__name__ == 'Week'):
        new.value = b.value * convertion[('day', 'week')] * convertion[('hour', 'day')]
    return new  # 'Day({})'.format(new.value)


# ===== add
def add_Coercion1(a, b):
    return 'Hour({})'.format(a + b)


def add_Coercion2(a, b):
    return 'Hour({})'.format((a + b) * convertion[('hour', 'day')])


def add_Coercion3(a, b):
    return 'Hour({})'.format((a + b) * convertion[('hour', 'day')] * convertion[('hour', 'day')])


# ===== sub
def sub_Coercion4(a, b):
    return 'Hour({})'.format(a.value - b.value)


def sub_Coercion5(a, b):
    return 'Hour({})'.format((a.value - b.value) * convertion[('hour', 'day')])


def sub_Coercion6(a, b):
    return 'Hour({})'.format((a.value - b.value) * convertion[('hour', 'day')] * convertion[('hour', 'day')])


coercions = {('day', 'hour'): DayToHour,
             ('week', 'day'): WeekToDay,
             ('week', 'hour'): WeekToHour}


def coerce_apply(operator_name, x, y):
    '''Generic function that performs the action after conversion of time to hours.'''
    tx, ty = type_tag(x), type_tag(y)

    if tx != ty:
        if (tx, ty) in coercions:
            x = coercions[(tx, ty)](x)
            tx = ty
            # print(x)
        elif (ty, tx) in coercions:
            y = coercions[(ty, tx)](y)
            ty = tx

        else:
            return 'No coercion possible.'
    assert tx == ty

    key = (operator_name, tx)
    # print(key)
    return coerce_apply.implementations[key](x, y)


coerce_apply.implementations = {  # ===== sum

    ('add', 'hour'): add_Coercion1,
    ('add', 'day'): add_Coercion2,
    ('add', 'week'): add_Coercion3,

    # ===== sub
    ('sub', 'hour'): sub_Coercion4,
    ('sub', 'day'): sub_Coercion5,
    ('sub', 'week'): sub_Coercion6
}


def DriverTask2C():
    # print(coercions[('day','hour')](Day(5)).__repr__())
    print(coerce_apply('add', Hour(50), Hour(2)))
    print(coerce_apply('sub', Week(1), Week(1)))


#DriverTask2C()


# ===================== Task 3 =====================

def make_class(name, attrs, base=None):
    """Return a new class (a dispatch dictionary) with given class attributes"""

    # print(attrs)
    # Getter: class attribute (looks in this class, then base)
    def get(name):
        if name in attrs:
            return attrs[name]
        elif base:
            return base['get'](name)

    # Setter: class attribute (always sets in this class)
    def set(name, value):
        attrs[name] = value

    def mro(cls):
        res = [cls['get']('type')]
        if base:
            res.extend([base['get']('type')])
        return res

    # Return a new initialized objec'aaa': 5.5t instance (a dispatch dictionary)
    def new(*args):
        # instance attributes (hides encapsulating function's attrs)
        attrs = {}

        # Getter: instance attribute (looks in object, then class (binds self if callable))
        def get(name):
            if name in attrs:
                return attrs[name]
            else:
                value = cls['get'](name)
                if callable(value):
                    return lambda *args: value(obj, *args)
                else:
                    return value

        # Setter: instance attribute (always sets in object)
        def set(name, value):
            attrs[name] = value

        # instance dictionary
        obj = {'get': get, 'set': set}

        # calls constructor if present
        init = get('__init__')
        if init: init(*args)

        return obj

    # class dictionary
    cls = {'get': get, 'set': set, 'new': new}
    # ===== solve a
    cls['set']('name', name)
    # ===== solve a
    # ===== solve b
    cls['set']('type', name)
    # ===== solve b
    cls['set']('this', cls)
    # ===== solve c
    cls['set']('mro', mro)
    # ===== solve c

    return cls


# ==========================================
def make_account_class():
    def __init__(self, owner):
        self['set']('owner', owner)

    return make_class("Account", locals())


def make_save_account_class():
    return make_class('SaveAccount', {}, make_account_class())


def DriverTask3():
    Account = make_account_class()
    print(Account['get']('name'))
    Jim = Account['new']('Jim')
    print(Jim['get']('type'))
    Bob = Jim['get']('this')['new']('Bob')
    print(Bob['get']('type'))
    SaveAccount = make_save_account_class()
    Jack = SaveAccount['new']('Jack')
    print(Jack['get']('type'))

    print(Jack['get']('mro')())


#DriverTask3()


# ===================== Task 4 =====================
from operator import add
from functools import reduce

def accumulate_tree(tree,fn):
    '''Recursive function returns the cumulative result of F on all the leaves in the'''
    return tree if type(tree) is not tuple else reduce(fn , (accumulate_tree(branch, fn) for branch in tree))

# ===================== Task 5 =====================


"""Calculator

An interpreter for a calculator language using prefix-order call syntax.
Operator expressions must be simple operator names or symbols.  Operand
expressions are separated by commas.

Examples:
    calc> mul(1, 2, 3)
    6
    calc> add()
    0
    calc> add(2, div(4, 8))
    2.5
    calc> add
    SyntaxError: expected ( after add
    calc> div(5)
    TypeError: div requires exactly 2 arguments
    calc> div(1, 0)
    ZeroDivisionError: division by zero
    calc> ^DCalculation completed.
"""

from functools import reduce
from operator import mul,add

def read_eval_print_loop():
    """Run a read-eval-print loop for calculator."""
    
    #solution 4.a
    global env 
    env = {}
    ###################
    while True:
        try:
            expression_tree = calc_parse(input('calc> '))
            """ solution"""
            if expression_tree:
                print(calc_eval(expression_tree))
            """ solution"""   
        except (SyntaxError, TypeError, ZeroDivisionError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):  # <Control>-D, etc. <ctrl-C>
            print('Calculation completed.')
            return

# Eval & Apply

class Exp(object):
    """A call expression in Calculator.
    
    >>> Exp('add', [1, 2])
    Exp('add', [1, 2])
    >>> str(Exp('add', [1, Exp('mul', [2, 3])]))
    'add(1, mul(2, 3))'
    """

    def __init__(self, operator, operands):
        self.operator = operator
        self.operands = operands

    def __repr__(self):
        return 'Exp({0}, {1})'.format(repr(self.operator), repr(self.operands))

    def __str__(self):
        operand_strs = ', '.join(map(str, self.operands))
        return '{0}({1})'.format(self.operator, operand_strs)

def calc_eval(exp):
    """Evaluate a Calculator expression.

    >>> calc_eval(Exp('add', [2, Exp('mul', [4, 6])]))
    26
    """
    if type(exp) in (int, float):
        return exp
    if type(exp) == Exp:
        arguments = list(map(calc_eval, exp.operands))
        return calc_apply(exp.operator, arguments)
    #solution 4.b
    if type(exp)==str:
        if exp in env:
            return env[exp]
        else:
            return NameError("'Unbound variable : "+exp)
    #####################
    
def calc_apply(operator, args):
    """Apply the named operator to a list of args.
    
    >>> calc_apply('+', [1, 2, 3])
    6
    >>> calc_apply('-', [10, 1, 2, 3])
    4
    >>> calc_apply('*', [])
    1
    >>> calc_apply('/', [40, 5])
    8.0
    """
    if operator in ('add', '+'):
        return sum(args)
    if operator in ('sub', '-'):
        if len(args) == 0:
            raise TypeError(operator + 'requires at least 1 argument')
        if len(args) == 1:
            return -args[0]
        return sum(args[:1] + [-arg for arg in args[1:]])
    if operator in ('mul', '*'):
        return reduce(mul, args, 1)
    if operator in ('div', '/'):
        if len(args) != 2:
            raise TypeError(operator + ' requires exactly 2 arguments')
        numer, denom = args
        return numer/denom

# Parsing

def calc_parse(line):
    """Parse a line of calculator input and return an expression tree."""
    tokens = tokenize(line)
    #solution 4
    if len(tokens) > 2 and tokens[1]=='=':
        execute(tokens)
    else:
    ###########
        expression_tree = analyze(tokens)
        if len(tokens) > 0:
            raise SyntaxError('Extra token(s): ' + ' '.join(tokens))
        return expression_tree

def tokenize(line):
    """Convert a string into a list of tokens.
    
    >>> tokenize('add(2, mul(4, 6))')
    ['add', '(', '2', ',', 'mul', '(', '4', ',', '6', ')', ')']
    """
    """ solution 4"""
    spaced = line.replace('(',' ( ').replace(')',' ) ').replace(',', ' , ').replace('=',' = ')
   ##################
    return spaced.strip().split()

known_operators = ['add', 'sub', 'mul', 'div', '+', '-', '*', '/']

def analyze(tokens):
    """Create a tree of nested lists from a sequence of tokens.

    Operand expressions can be separated by commas, spaces, or both.
    
    >>> analyze(tokenize('add(2, mul(4, 6))'))
    Exp('add', [2, Exp('mul', [4, 6])])
    >>> analyze(tokenize('mul(add(2, mul(4, 6)), add(3, 5))'))
    Exp('mul', [Exp('add', [2, Exp('mul', [4, 6])]), Exp('add', [3, 5])])
    """
    assert_non_empty(tokens)
    token = analyze_token(tokens.pop(0))
    if type(token) in (int, float):
        return token
    if token in known_operators:
        if len(tokens) == 0 or tokens.pop(0) != '(':
            raise SyntaxError('expected ( after ' + token)
        return Exp(token, analyze_operands(tokens))
    #solurion 4
    else:
        #raise SyntaxError('unexpected ' + token)
        return token

def analyze_operands(tokens):
    """Analyze a sequence of comma-separated operands."""
    assert_non_empty(tokens)
    operands = []
    while tokens[0] != ')':
        if operands and tokens.pop(0) != ',':
            raise SyntaxError('expected ,')
        operands.append(analyze(tokens))
        assert_non_empty(tokens)
    tokens.pop(0)  # Remove )
    return operands

def assert_non_empty(tokens):
    """Raise an exception if tokens is empty."""
    if len(tokens) == 0:
        raise SyntaxError('unexpected end of line')

def analyze_token(token):
    """Return the value of token if it can be analyzed as a number, or token.
    
    >>> analyze_token('12')
    12
    >>> analyze_token('7.5')
    7.5
    >>> analyze_token('add')
    'add'
    """
    try:
        return int(token)
    except (TypeError, ValueError):
        try:
            return float(token)
        except (TypeError, ValueError):
            return token
# solution 4.c
def execute(tokens):
    letter=tokens.pop(0) # letter = n
    tokens.pop(0)
    expression_tree=analyze(tokens) #conversion
    if len(tokens)>0:
        raise SyntaxError('Extra token(s): ' + ' '.join(tokens))
    env[letter]=calc_eval(expression_tree) # using global from section 4.a
def run():
    read_eval_print_loop()
    
#run()




