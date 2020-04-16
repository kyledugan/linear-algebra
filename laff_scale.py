import numpy as np

def laff_scale(alpha,x):
    # check that a 2D array is passed in
    if len(x.shape) != 2:
        return 'FAILED'
    
    # check that alpha is an interger
    if not isinstance(alpha, int):
        return 'FAILED'
        
    mx, nx = x.shape
    
    # check that x is a vector
    if mx != 1 and nx != 1:
        return 'FAILED'
    
    if mx == 1: # x is a row vector
        for i in range(nx):
            x[0][i] = x[0][i] * alpha
    else: # x is a column vector
        for i in range(mx):
            x[i][0] = x[i][0] * alpha

    return x

x = np.array([[1,2,3]])
y = np.array([4,5,6])
z = np.array([[7],[8],[9]])
print(laff_scale(2, y))