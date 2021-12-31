from math import *

def f(x):
    #return (x*x*x)-sin(x)+cos(x)    # один корень
    #return (x*x*x*x)-sin(x)-cos(x) # два корня
    #return (x*x*x)+100*sin(x)+5    # пять корней
    #return 4                       # нет корней
    return (x*x*x*x)+10*(x*x*x)-1

def dx(f, x): #насколько значение функции близко к 0; оценка насколько x явл корнем
    return abs(0-f(x))

def dixotomia(f, x1, x2, e):
    n=0
    xc=(x1+x2)/2
    delta = dx(f, xc)
    while delta > e:
        n+=1
        if (f(xc)*f(x1) < 0):
            x2 = xc
        else:
            x1 = xc
        xc=(x1+x2)/2
        delta = dx(f, xc)
    print('---------------------------')
    print(m+1,'корень:')
    print ('x = ', xc)
    print ('Погрешность f(x) = ', f(xc))    # насколько f(x) отличается от 0
    print ('Количество итераций = ', n)
    print('---------------------------')

def otdelenie_korney(a,b,n): #нахождение интервалов где функция меняет знак
    L=[]
    h=(b-a)/n
    x1=a
    while (x1 <= b):
        x2=x1+h
        if (f(x1)*f(x2)<0):
            L+=[(x1,x2)]
        x1=x2
    if (L==[]):
        print('Корней нет')
        exit
    return L

#начальные условия
a=-100
b=100
n=1000
e = 1.0e-12

L=otdelenie_korney(a,b,n)
print("----------------12")
print(L)

m=0
for x in L:
    x1=L[m][0]
    x2=L[m][1]
    dixotomia(f, x1, x2, e)
    m+=1







