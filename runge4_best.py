from math import *
from numpy import arange
import matplotlib.pyplot as plt

# Решение уравнения x'' + 2kx' + c*c*x = 0       x(0)=0      x'(0)=1
# x' = v
# x'' = v' = f(x, v, t)

a=5.0
b=12*pi
n=4000     
h=(b-a)/n

k=0.05        # при k=0 уравнение x'' + x = 0 является уравнением гармонических колебаний
c=1.0

def f(x, v, t):
    return -2*k*v-c*c*x

tpoints = arange(a,b,h)
xpoints = []
vpoints = []

x=0.0     # x(0)
v=1.0     # v(0)=x'(0)

for t in tpoints:
    xpoints.append(x)
    vpoints.append(v)    

    m1 = h*v
    k1 = h*f(x, v, t)

    m2 = h*(v + 0.5*k1)
    k2 = h*f(x+0.5*m1, v+0.5*k1, t+0.5*h)

    m3 = h*(v + 0.5*k2)
    k3 = h*f(x+0.5*m2, v+0.5*k2, t+0.5*h)

    m4 = h*(v + k3)
    k4 = h*f(x+m3, v+k3, t+h)

    x += (m1 + 2*m2 + 2*m3 + m4)/6
    v += (k1 + 2*k2 + 2*k3 + k4)/6


# Построение графика x(t) -------------------------------------------
plt.subplot(1,3,1)
plt.plot(tpoints,xpoints)
plt.grid()
plt.title('Зависимость x(t)')
plt.xlabel('t (c)')
plt.ylabel('x (м)')
#plt.show()

# Построение графика V(t) -------------------------------------------
plt.subplot(1,3,2)
plt.plot(tpoints, vpoints)
plt.grid()
plt.title('Зависимость V(t)')
plt.xlabel('t (c)')
plt.ylabel('V (м/с)')
#plt.show()

# Построение графика V(x) (фазовый портрет) -------------------------
plt.subplot(1,3,3)
plt.plot(xpoints,vpoints)
plt.grid()
plt.title('Фазовый портрет V(x)')
plt.xlabel('X (м)')
plt.ylabel('V (м/c)')
plt.tight_layout()
plt.show()

