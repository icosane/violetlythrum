from math import *
import matplotlib.pyplot as plt
def f(x, y): 
    return (x + y + x * y) 

m = []
z = []
#начальные условия
x = 0
y = 1
N = 40 #число отрезков разбиения

h = abs((x-y)/N)

def euler(f, x, y, h, n):
    for i in range(1,n+1):
        xk = x + h
        y = y + h * f(x, y)
        z.append(y)
        x = xk
        m.append(x)
        print("Решение для y = "+str(y)+" от x= "+str(x)+" получено за "+str(i)+" итераций")

euler(f,x,y,h,N)
for i in range(N):
    plt.plot(m, z)
plt.grid()
plt.xlabel('x')
plt.ylabel('y(x)')
plt.show()
