 
#T1
cube=lambda x: x*x*x 
def simpson_rule(f,a,b,n):  
    ''' The function calculate the integral of a cube according to Simpson's rule.'''

    Sum=0
    h=(b-a)/n
    for k in range (1,n):
        Yk=a+k*h
        if k%2==0:
            Sum+=2*f(Yk)
        else:
            Sum+=4*f(Yk)
    simpson_integral=h/3.0*(f(a)+f(b)+Sum)
    return simpson_integral
      
help(simpson_rule)  
print(simpson_rule(cube,0,1,100))
  

#T2
square=lambda x:x**2    
def repeated(f,n):
    ''' The repeating function is restore the n activation of F.'''

    def compose(f,g):
        return lambda x: f(g(x))
      
    g = f
    for _ in range (1,n):
        f = compose(f, g)
    return f
   
help(repeated)
print(repeated(square,2)(5))
   


#T3
def smooth(f,dx = 1e-6):
    ''''The function return a strong function of f.'''
    def smooth2(x):
        return (f(x-dx)+f(x)+f(x+dx))/3
    return smooth2
help(smooth)
smoothed = smooth(square)
print(smoothed(2))

def n_fold_smooth(f,n):
    '''The function accepts the smoothing of n Function f using the Rip function'''

    return repeated(smooth,n)(f)

help(n_fold_smooth)
sn= n_fold_smooth(lambda x:x*x, 3)
print(sn(2))
