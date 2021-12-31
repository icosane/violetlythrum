from math import *

from numpy import arange
import matplotlib.pyplot as plt

# Решение уравнения x'' + 2gx' + w*w*x = 0       x(0)=5      x'(0)=1
# x' = v
# x'' = v' = f(x, v, t)

a=5.0
b=12*pi
n=4000     # очень большое количество разбиений из-за медленной сходимости метода Эйлера, имеющего первый порядок сходимости
h=(b-a)/n

g=0.05      # при g=0 уравнение x'' + x = 0 является уравнением гармонических колебаний 
w=1.0

def f(x, v, t):
    return -2*g*v-w*w*x

tpoints = arange(a,b,h)
xpoints = []
vpoints = []

x=0.0     # x(0)
v=1.0     # v(0)=x'(0)

for t in tpoints:
    xpoints.append(x)
    vpoints.append(v)

    x_pred=x                   # предыдущее (старое) значение x
    x+=h*v                     # x=x+h*x'   x(i)=x(i-1)+h*x'(i-1)
    v+=h*f(x_pred,v,t)         # v=x'

plt.subplot(1,3,1) 
plt.plot(tpoints,xpoints)
plt.grid()
plt.title('Зависимость x(t)')
plt.xlabel('t (c)')
plt.ylabel('x (м)')
#plt.show()
# Построение графика V(t) -------------------------------------------
plt.subplot(1,3,2) 
plt.plot(tpoints,vpoints)
plt.grid()
plt.title('Зависимость V(t)')
plt.xlabel('t (c)')
plt.ylabel('V (м/c)')
#plt.show()

# Построение графика V(x) (фазовый портрет) -------------------------
plt.subplot(1,3,3) 
plt.plot(xpoints,vpoints)
plt.grid()
plt.title('Фазовый портрет V(x)')
plt.xlabel('X (м)')
plt.ylabel('V (м/c)')
plt.tight_layout() #чтобы не накладывалось друг на друга
plt.show() 

