a = 0
def f1(x):
    def f2(y):
        nonlocal x
        x = x * 2
        return x > y
    def f3(y):
        global a
        a = a + 1
        return a + y
    def f4(y):
        print("y ---> ",y)
        nonlocal x
        x = x + 1
        return y + x

    y = 'a'
    if f2(x):
        y = f3(x)
    print('a={0}, x={1}, y={2}'.format(a, x, y))
    return f4;

f1(5)(10)

