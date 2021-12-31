from math import *
from numpy import arange
import matplotlib.pyplot as plt

# Решение уравнения x' + 5(t^3)x = 0       x(-1.5)=0.01
# x' = = f(x, t)

a=-1.5
b=1.5
n=400
h=(b-a)/n

def f(t,x):
    return -5*t*t*t*x

tpoints = arange(a,b,h)
xpoints = []
vpoints = []

x=0.01     # x(-1.5)
v=-0.16875

for t in tpoints:
    xpoints.append(x)
    vpoints.append(v)

    v=f(t,x)

    k1=h*f(t,x)

    k2=h*f(t+0.5*h, x+0.5*k1)

    k3=h*f(t+0.5*h, x+0.5*k2)

    k4=h*f(t+h, x+k3)

    x+=(k1+2*k2+2*k3+k4)/6.0

# Построение графика x(t) -------------------------------------------

plt.plot(tpoints,xpoints)
plt.grid()
plt.title('Зависимость x(t)')
plt.xlabel('t (c)')
plt.ylabel('x (м)')
plt.show()

# Построение графика V(t) -------------------------------------------

plt.plot(tpoints, vpoints)
plt.grid()
plt.title('Зависимость V(t)')
plt.xlabel('t (c)')
plt.ylabel('V (м/с)')
plt.show()

# Построение графика V(x) (фазовый портрет) -------------------------

plt.plot(xpoints,vpoints)
plt.grid()
plt.title('Фазовый портрет V(x)')
plt.xlabel('X (м)')
plt.ylabel('V (м/c)')
plt.show()






