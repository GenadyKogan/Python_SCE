from operator import add,sub
### ---bet Q1 ---###
def is_binary(tree):
    if type(tree) != tuple:
        return True
    if len(tree) != 2:
        return False
    return is_binary(tree[0]) and is_binary(tree[1])

# print(is_binary(((2, 3), (4, (5, 6)))))
# True
# print(is_binary((2, (3, (4, 5, 6)))))
# False

def filter_tree(f, tree):
    return tuple(el for el in tree if type(el)!=tuple and f(el)) + tuple(filter_tree(f, el) for el in tree if type(el)==tuple)

#print(filter_tree(lambda x: x%2==0, (1, 2, (3,4,5),6,7)))
#print(filter_tree(lambda x: x%2==0, (1, 2, (3,4,(8,9),5),6,7)))


### --- Q3 ---
from functools import reduce
wordnet = ('catapulta', 'caput', 'catephant')
w1,w2 = 'cat','elephant'
prefixes = lambda w: tuple(map(lambda i: w[:i], range(1,len(w)+1)))
#print(prefixes(w1))
suffixes = lambda w: tuple(map(lambda i: w[i:], range(0,len(w))))
#print(suffixes(w2))
concats = lambda a,lst: tuple(map(lambda x: x+a, lst))
#print(concats('aa',('bb','cc','dd')))
all_concats = lambda lst1, lst2: tuple(map(lambda x: concats(x,lst1), lst2))
#print(all_concats(('aa','bb'),('c','d','e')))
all_concats_flat = lambda lst1, lst2: reduce(add, all_concats(lst1,lst2))
#print(all_concats_flat(('aa','bb'),('c','d','e')))
words_generator = lambda w1, w2: all_concats_flat(prefixes(w1),suffixes(w2))
#print(words_generator(w1,w2))
words = lambda w1,w2: tuple(filter(lambda x: x in wordnet, words_generator(w1,w2)))
#print(words(w1,w2))

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
    ### initialize GLOBAL environment ###
    global env
    env = {}
    ##############################
    while True:
        try:
            row = input('calc> ')
            expression_tree = calc_parse(row)
            ### avoid printing 'None' ###
            if expression_tree:
                #############################
                print(calc_eval(expression_tree))
        except (SyntaxError, TypeError, ZeroDivisionError, NameError) as err:
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
    ### if token is variable ###
    elif type(exp) == str:
        if exp in env:
            return env[exp]
        else:
            raise NameError('unbound variable ' + exp)

def calc_apply(operator, args):
    #alef
    if len(args) == 0:
            raise TypeError('all operators require at least 1 argument')
    #alef
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
##        if len(args) == 0:
##            raise TypeError(operator + 'requires at least 1 argument')
        if len(args) == 1:
            return -args[0]
        return sum(args[:1] + [-arg for arg in args[1:]])
    if operator in ('mul', '*'):
        return reduce(mul, args, 1)
    if operator in ('div', '/'):
        if len(args) != 2:
            raise TypeError(operator + ' requires exactly 2 arguments')
        numer, denom = args
        return float(numer)/denom

# Parsing

def calc_parse(line):
    """Parse a line of calculator input and return an expression tree."""
    tokens = tokenize(line)
    if len(tokens)>2 and tokens[1] == '=':
        #gimel
        if tokens[0] in known_operators:
            raise SyntaxError('variable cannot get name of an operator: ' + tokens[0])
        if not tokens[0].isalpha():
            raise SyntaxError('variable name cannot contain non-alphabetical symbols: ' + tokens[0])
        else:
            execute(tokens)
    else:
        expression_tree = analyze(tokens)
        if len(tokens) > 0:
            raise SyntaxError('Extra token(s): ' + ' '.join(tokens))
        return expression_tree

def tokenize(line):
    """Convert a string into a list of tokens.
    
    >>> tokenize('add(2, mul(4, 6))')
    ['add', '(', '2', ',', 'mul', '(', '4', ',', '6', ')', ')']
    """
     ### .replace('=',' = ') ###
    spaced = line.replace('(',' ( ').replace(')',' ) ').replace(',', ' , ').replace('=',' = ')
    ###
    #OR
    # spaced = line.replace('=',' = ')
    ###
    return spaced.strip().split()

known_operators = ['add', 'sub', 'mul', 'div', '+', '-', '*', '/']

def execute(tokens):
    var = tokens.pop(0)
    tokens.pop(0) # remove '='
    expression_tree = analyze(tokens)
    if len(tokens) > 0:
        raise SyntaxError('Extra token(s): ' + ' '.join(tokens))
    env[var]=calc_eval(expression_tree)

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
    #print('token ---> ',token)
    if type(token) in (int, float):
        return token
    if token in known_operators:
        if len(tokens) == 0 or tokens.pop(0) != '(':
            raise SyntaxError('expected ( after ' + token)
        return Exp(token, analyze_operands(tokens))
    else:
        raise SyntaxError('unexpected ' + token)

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
       # print('int(token) ---> ',int(token))
        return int(token)
    except (TypeError, ValueError):
        try:
            return float(token)
        except (TypeError, ValueError):
            return token

def run():
    read_eval_print_loop()

run()

