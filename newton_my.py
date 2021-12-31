from math import *

def f(x):
    #return (x*x*x)-sin(x)+cos(x)
    #return (x*x*x*x)-sin(x)-cos(x)
    return (x*x*x)+100*sin(x)+5
    #return 20*(x*x)+6*x-50
def df(x):
    #return (3*x*x)-sin(x)-cos(x)
    #return (4*x*x*x)+sin(x)-cos(x)
    return (3*x*x)+100*cos(x)
    #return 40*x+6
def d2f(x):
    #return (6*x)+sin(x)-cos(x)
    #return (12*x*x)+sin(x)+cos(x)
    return (6*x)-100*sin(x)
    #return 40
def dx(f, x):
    return abs(0-f(x))

def newtons_method(f, df, x0, e):
    n=0
    delta = dx(f, x0)
    while delta > e:
        n+=1
        if (abs(df(x0))<1.0e-15):
            print('Первая производная равна 0. Метод не применим.')
            exit()
        else:
            x0 = x0 - f(x0)/df(x0)
        delta = dx(f, x0)
    print('---------------------------')
    print(m+1,'корень:')
    print ('x = ', x0)
    print ('Погрешность f(x) = ', f(x0))    # насколько f(x) отличается от 0
    print ('Количество итераций = ', n)

def otdelenie_korney(a,b,n): #нахождение интервалов где функция меняет знак
    L=[]
    dx1=(b-a)/n
    x1=a
    while (x1 <= b):
        x2=x1+dx1
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

m=0
for x in L: #выбор граничной точки 
    x1=x[0]
    x2=x[1]
    if (f(x1)*d2f(x1)>0):
        x0=x1
    elif (f(x2)*d2f(x2)>0):
        x0=x2
    else:
    
        x0=x1
    newtons_method(f, df, x0, e)
    m+=1







