from math import *
e = 0.001
def f(x):
    return (x*x*x)-sin(x)+cos(x)
a = -10
b = 2
def dixotomia(a,b,c):
    while (abs(b - a) > e):
        c = (a+b)/2
        if ((f(b)*f(c))<0):
            a = c
        else:
            b = c
            c = (a+b)/2
    else:
        print('нет корней')
x = (a+b)/2
print ('x=',x,'f(x)=',f(x))