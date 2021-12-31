from math import *
import numpy as np
import matplotlib.pyplot as plt

T=2*pi #конец интервала, начало интервала = 0
m=5 #количество узлов интерполяции
j=int((m/2)-0.5) # J < (m/2) число коэф a & b для прямого преобразования
n=int((m/2)-0.5) # n < (m/2) количество тригонометрических полиномов в обратном преобразовании 

#задание узлов интерполяции
x=np.zeros(m)
for k in range(m): #создание списка xk=kT/m
    x[k]=k*T/m

y=np.zeros(m)
for i in range(m): #значение функции yk
    y[i]=x[i]*sin(x[i])

#расчет коэффициентов преобразования A & B для прямого преобразования 
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

#расчет обратного дискретного преобразования Фурье
def f(x):
    S=0
    for j in range(1,n+1):
        S=S+(A(j)*cos(2*pi*j*x/T)+B(j)*sin(2*pi*j*x/T))
    S=S+(A(0)/2)
    return S

yf=np.zeros(m) #значения функции в узлах полученные интерполяцией    
for i in range(m):
    yf[i]=f(x[i])

z=abs(y-yf) #разность экспериментального и найденного интерполяцией значений

print(z)
print('======================================')
print('Максимальное расхождение в узлах равно ',(max(z)))
print('======================================')

plt.plot(x,y,'o', label = 'экспериментальные значения')
plt.plot(x, yf, '-', label = 'интерполированные значения') #o - эксп, "-" - полученные
plt.grid()
plt.legend()
plt.show()

x=4.8
print('Промежуточное значение x = ',x,'\n')

print('Точное значение y(',x,')=',x*sin(x))
print('Интерполяция    y(',x,')=',f(x))



