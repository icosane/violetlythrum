import numpy as np

def TDMAsolver(a, b, c, d):
    n = len(a) #number of equations
    ac, bc, cc, dc = (x.astype(float) for x in (a, b, c, d)) #copy arrays
    for i in range(1, n):
        mc = ac[i-1]/bc[i-1]
        bc[i] = bc[i] - mc*cc[i-1] 
        dc[i] = dc[i] - mc*dc[i-1]
    xc = bc
    xc[-1] = dc[-1]/bc[-1]

    for i1 in range(n-2, -1, -1):
        xc[i1] = (dc[i1]-cc[i1]*xc[i1+1])/bc[i1]

    return xc

#( 3 2 0 0 )   ( x0 )   ( 12 )
#( 2 3 2 0 ) . ( x1 ) = ( 17 )
#( 0 2 3 2 )   ( x2 )   ( 14 )
#( 0 0 2 3 )   ( x3 )   (  7 )

#( b0 c0 0  0  )   ( x0 )   ( d0 )
#( a0 b1 c1 0  ) . ( x1 ) = ( d1 )
#( 0  a1 b2 c2 )   ( x2 )   ( d2 )
#( 0  0  a2 b3 )   ( x3 )   ( d3 )

a = np.array([2,2,2])
b = np.array([3,3,3,3]) # main diagonal
c = np.array([2,2,2])
d = np.array([12,17,14,7]) # right side of equation

x = TDMAsolver(a,b,c,d) # pass in same order
print(x)

A = np.diag(b,0) + np.diag(a,-1) + np.diag(c,1)
x = np.linalg.solve(A,b)
print(x)