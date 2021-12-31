from math import *
def f(x):
    #return (x*x*x)-sin(x)+cos(x)
    return (x*x)-2

def df(x):
    #return (3*x*x)-sin(x)-cos(x)
    return 2*x
def dx(f, x):
    return abs(0-f(x))

def newtons_method(f, df, x0, e):
    delta = dx(f, x0)
    while delta > e:
        x0 = x0 - f(x0)/df(x0)
        delta = dx(f, x0)
    print ('x = ', x0)
    print ('f(x) = ', f(x0))

x0s = [-1, 2]
e = 0.00001
for x0 in x0s:
    newtons_method(f, df, x0, e)

