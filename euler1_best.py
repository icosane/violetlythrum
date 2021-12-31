from math import *
from numpy import arange
import matplotlib.pyplot as plt

# Решение уравнения t**2 - x**3 = 0       x(-1.5)=0.01
# x' = = f(x, t)

a=-1.5
b=1.5
n=100000     # очень большое количество разбиений из-за медленной сходимости метода Эйлера, имеющего первый порядок сходимости
h=(b-a)/n

def f(x,t):
    return t**2 - x**3

tpoints = arange(a,b,h)
xpoints = []
vpoints = []

x=1     # x(-1.5)
v=-0.16875

for t in tpoints:
    xpoints.append(x)
    vpoints.append(v)

    v=f(x,t)           # v=x'
    x+=h*f(x,t)



# Построение графика x(t) -------------------------------------------

plt.plot(tpoints,xpoints)
plt.grid()
plt.title('Зависимость x(t)')
plt.xlabel('t (c)')
plt.ylabel('x (м)')
plt.show()

# Построение графика V(t) -------------------------------------------

plt.plot(tpoints,vpoints)
plt.grid()
plt.title('Зависимость скорости от времени V(t)')
plt.xlabel('t (c)')
plt.ylabel('V (м/c)')
plt.show()

# Построение графика V(x) (фазовый портрет) -------------------------

plt.plot(xpoints,vpoints)
plt.grid()
plt.title('Фазовый портрет V(x)')
plt.xlabel('X (м)')
plt.ylabel('V (м/c)')
plt.show()