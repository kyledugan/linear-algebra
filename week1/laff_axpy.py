import numpy as np

def laff_axpy(alpha,x,y):
    # check that 2D arrays are passed in
    if len(x.shape) != 2 or len(y.shape) != 2:
        return 'FAILED'
    
    # check that alpha is an interger
    if not isinstance(alpha, int):
        return 'FAILED'
        
    mx, nx = x.shape
    my, ny = y.shape
    
    # check that both inputs are vectors
    if (mx != 1 and nx != 1) or (my != 1 and ny != 1):
        return 'FAILED'
    # check that both vectors have same number of elements
    if mx * nx != my * ny:
        return 'FAILED'
    
    if mx == 1 and my == 1: # both are row vectors
        for i in range(nx):
            y[0][i] += alpha * x[0][i].copy()
    elif nx == 1 and ny == 1: # both are column vectors
        for i in range(mx):
            y[i][0] += alpha * x[i][0].copy()
    elif my == 1: # x is a column vector and y is a row vector
        for i in range(mx):
            y[0][i] += alpha * x[i][0].copy()
    else: # x is a row vector and y is a column vector
        for i in range(nx):
            y[i][0] += alpha * x[0][i].copy()

    return y

x = np.array([[1,2,3]])
y = np.array([[4,5,6]])
z = np.array([[7],[8],[9]])
zz = np.array([[10], [11], [12]])
print(laff_axpy(3,zz,x))