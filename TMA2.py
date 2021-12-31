import numpy as np
#a = Lower Diag, b = Main Diag, c = Upper Diag, d = solution vector
#matrix checking
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

print(f"Matrix is tridiagonal? {tridiagonal}")

a = np.array([2,2,2])
b = np.array([3,3,3,3]) # main diagonal
c = np.array([2,2,2])
d = np.array([12,17,14,7])
def TDMA(a,b,c,d):
    n = len(d)
    w= np.zeros(n-1,float) #возвращает матрицу заполненную нулями
    g= np.zeros(n, float)
    p = np.zeros(n,float)

    w[0] = c[0]/b[0]
    g[0] = d[0]/b[0]

    for i in range(1,n-1):
        w[i] = c[i]/(b[i] - a[i-1]*w[i-1])
    for i in range(1,n):
        g[i] = (d[i] - a[i-1]*g[i-1])/(b[i] - a[i-1]*w[i-1])
    p[n-1] = g[n-1]
    for i in range(n-1,0,-1):
        p[i-1] = g[i-1] - w[i-1]*p[i]
    return p

x = TDMA(a,b,c,d) # pass in same order
print(x) 

