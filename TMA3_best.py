import numpy as np
#a = нижняя диагональ, b = главная диагональ, c = верхняя диагональ, f = вектор решений
#проверка является ли матрица подходящей
matrix = [
    [ 3,2,0,0 ],
    [ 2,3,2,0 ],  
    [ 0,2,3,2 ],
    [ 0,0,2,3 ]
]

tridiagonal = True

for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if y >= x - 1 and y <= x + 1:
            if matrix[x][y] == 0:
                tridiagonal = False
                break 
        else:
            if matrix[x][y] != 0:
                tridiagonal = False
                break 
    if not tridiagonal:
        break 

print(f"Матрица трехдиагональная {tridiagonal}")

a = np.array([2,2,2]) #нижняя диагональ
b = np.array([3,3,3,3]) # главная диагональ
c = np.array([2,2,2]) #верхняя диагональ
f = np.array([12,17,14,7])
def TDMA(a,b,c,f):
    if (tridiagonal == False):
        print("Алгоритм не подходит для данной матрицы.")
        exit()
    n = len(f)
    alpha = np.zeros(n-1,float) 
    beta= np.zeros(n, float)
    x = np.zeros(n,float)

    alpha[0] = a[0]/b[0]
    beta[0] = f[0]/b[0]

#ищем прямым ходом коэфициенты 
    for i in range(1,n-1): #прямой ход 
        alpha[i] = a[i]/(b[i] - c[i-1]*alpha[i-1]) 
    for i in range(1,n): #прямой ход 
        beta[i] = (f[i] - c[i-1]*beta[i-1])/(b[i] - c[i-1]*alpha[i-1])
    x[n-1] = beta[n-1]
    for i in range(n-1,0,-1): #обратный ход вычисление корней
        x[i-1] = beta[i-1] - alpha[i-1]*x[i] #Xn–1 = AnXn + βn 
    return x

x = TDMA(a,b,c,f) 
for i in (range(len(f))):
    print("x"+str(i+1),end=" ")
print("= ",x)

