from math import *

def f(x):
    return (x*x*x*x)+10*(x*x*x)-1
def df(x):
    return 4*(x*x*x)+30*(x*x)
def d2f(x):
    return 12*(x*x)+60*x
def dx(f, x):
    return abs(0-f(x))

def newtons_method(f, df, x0):
    n=2 #Количество итераций
    for q in range(0,n):
        if (abs(df(x0))<1.0e-15):
            print('Первая производная равна 0. Метод не применим.')
            exit()
        else:
            x0 = x0 - f(x0)/df(x0)
        
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

L=[(0.0,1.0)] #интервал
x0 = 1 #начальное приближение
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
    newtons_method(f, df, x0)
    m+=1







