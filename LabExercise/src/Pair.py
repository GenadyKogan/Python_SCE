def make_pair(x, y):
    """Return a function that behaves like a pair."""
    def dispatch(m):
        if m == 0:
            return x
        elif m == 1:
            return y
    return dispatch
def getitem_pair(p, i):
        """Return the element at index i of pair p."""
        return p(i)
p = make_pair(1, 2)
print(getitem_pair(p, 0))