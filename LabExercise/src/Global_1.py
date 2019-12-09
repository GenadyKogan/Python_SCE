def identity(k):return k
def successor(k):return k+1
def cube(k):return pow(k,3)
def pi_term(k):return 8/(k*(k+2))
def pi_next(k):return k+4
def sum_cubes(n):return summation(n, cube, successor)
def summation(n, term, next):
        total, k = 0, 1
        while k <= n:
            total, k = total + term(k), next(k)
            #print("next ---> ",next(k))
            #print("total ---> ",total)
        return total
def sum_naturals(n):
    return summation(n, identity, successor)
def pi_sum(n):
        return summation(n, pi_term, pi_next)

f = lambda x:x*x
g = lambda x :x+1
z=(lambda f,g:lambda x :f(g(x)))(f,g)
print(z(2))
