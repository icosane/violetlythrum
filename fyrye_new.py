from math import *
import numpy as np
from numpy import *
from numpy import arange
import matplotlib.pyplot as plt

T=2*pi
m=10
j=int(m/2) # J < (m/2)
n=int(m/2) # n < (m/2)

x=np.zeros(m)
for k in range(m):
    x[k]=k*T/m

y=np.zeros(m)
for i in range(m):
    y[i]=x[i]*sin(x[i])

def A(j):
    S=0
    for k in range(m):
        S=S+y[k]*cos(2*pi*k*j/m)
    return (2/m)*S

def B(j):
    S=0
    for k in range(m):
        S=S+y[k]*sin(2*pi*k*j/m)
    return (2/m)*S

def f(x):
    S=0
    for j in range(1,n+1):
        S=S+(A(j)*cos(2*pi*j*x/T)+B(j)*sin(2*pi*j*x/T))
    S=S+(A(0)/2)
    return S

yf=np.zeros(m)
for i in range(m):
    yf[i]=f(x[i])

z=abs(y-yf)

print(z)

print('======================================')
print('Максимальное расхождение в узлах равно ',(max(z)))
print('======================================')

# --------------------------------------------------------------

L=500
xpoints = arange(0,T,(T/(L)))
ypoints = []

for xn in xpoints:
    ypoints.append(f(xn))

plt.plot(x,y,'o',xpoints, ypoints, '-')
plt.grid()
plt.show()

# -----------------------------------------------------------------


x=2.4
print('Промежуточное значение x = ',x,'\n')

print('Точное значение y(',x,')=',x*sin(x))
print('Интерполяция    y(',x,')=',f(x))



