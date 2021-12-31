from math import *
e = 0.001
def f(x):
    #return (x*x*x)-sin(x)+cos(x)
    return x*sin(x)
a = -10
b = 2
N = 12

def dixotomia(f,a,b,N):
    if f(a)*f(b) >= 0:
        print("Границы отрезков заданы неверно\n","Невозможно вычислить корень.")
    for n in range(1,N+1):
        c = (a + b)/2
        f_c = f(c)
        if f(a)*f_c < 0:
            a = a
            b = c
        elif f(b)*f_c < 0:
            a = c
            b = b
        elif f_c == 0:
            print("x = ")
            return c
        else:
            print("Невозможно вычислить корень.")
    return (a + b)/2
print(dixotomia(f,a,b,N))