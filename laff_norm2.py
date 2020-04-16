import numpy as np
from laff_dot import laff_dot

def laff_norm2(x):
    return laff_dot(x,x) ** 0.5

    # check that a 2D array is passed in
    # if len(x.shape) != 2:
    #     return 'FAILED'
        
    # mx, nx = x.shape
    
    # # check that x is a vector
    # if (mx != 1 and nx != 1):
    #     return 'FAILED'
    
    # total = 0
    # if mx == 1: # row vector
    #     for i in range(nx):
    #         total += x[0][i]**2
    # else: # column vector
    #     for i in range(mx):
    #         total += x[i][0]**2

    # return total**0.5

x = np.array([[1,5]])
y = np.array([[4,5,6]])
z = np.array([[7],[8],[9]])
print(laff_norm2(x))
print(np.linalg.norm(x) == laff_norm2(x))