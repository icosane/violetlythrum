from math import *
e = 0.001
def f(x):
    return (x*x*x)-sin(x)+cos(x)
    #return x*sin(x)
a = -10
b = 2

def dixotomia(a,b):  
    if (f(a) * f(b) >= 0): 
        print("Границы отрезков заданы неверно\n","Невозможно вычислить корень")
   
    c = a 
    while (abs(b - a) > e):
        c = (a+b)/2 #середина отрезка
        if (f(c)*f(a) < 0): 
            b = c 
        else: 
            a = c
    print("x = ","%.4f"%c, "\n", 'f(x)=',f(c) )
dixotomia(a, b)