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

def TDMA(a,b,c,f):
    a, b, c, f = map(lambda k_list: map(float, k_list), (a, b, c, f))

    alpha = [0]
    beta = [0]
    n = len(f)
    x = [0] * n

    for i in range(n-1):
        alpha.append(-b[i]/(a[i]*alpha[i] + c[i]))
        beta.append((f[i] - a[i]*beta[i])/(a[i]*alpha[i] + c[i]))
            
    x[n-1] = (f[n-1] - a[n-2]*beta[n-1])/(c[n-1] + a[n-2]*alpha[n-1])

    for i in reversed(range(n-1)):
        x[i] = alpha[i+1]*x[i+1] + beta[i+1]
    
    return x

# small test. x = (1,2,3)
if __name__ == '__main__':
    a = [3,3]
    b = [2,1]
    c = [6,5,8]
    f = [10,16,30]
    print(TDMA(a,b,c,f))