from math import *

def f(x):
    return (1/(1+x*x))
    #return (x*x*x*x)

def simpson(f, a, b, n):

    h=(b-a)/n

    s=f(a)+f(b) #сумма начального и конечного значений

    for k in range(1, n, 2):
       s += 4 * f(a + k * h) #нечетные

    for k in range(2, n-1, 2): 
       s += 2 * f(a + k * h) #четные

    return s * h / 3


a = 0
b = 1
int1 = simpson(f,a,b,8)
int2 = simpson(f,a,b,16)
print(int1)
print(int2)

int1 = int2
int2 = simpson(f,a,b,32)
print(int1)
print(int2)

int1 = int2
int2 = simpson(f,a,b,64)
print(int1)
print(int2)