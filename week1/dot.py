import numpy as np

def dot(x,y):
    # check that 2D arrays are passed in
    if len(x.shape) != 2 or len(y.shape) != 2:
        return 'FAILED'
        
    mx, nx = x.shape
    my, ny = y.shape
    dot = 0
    
    # check that both inputs are vectors
    if (mx != 1 and nx != 1) or (my != 1 and ny != 1):
        return 'FAILED'
    # check that both vectors have same number of elements
    if mx * nx != my * ny:
        return 'FAILED'
    
    if mx == 1 and my == 1: # both are row vectors
        for i in range(nx):
            dot += x[0][i] * y[0][i]
    elif nx == 1 and ny == 1: # both are column vectors
        for i in range(mx):
            dot += x[i][0] * y[i][0]
    elif my == 1: # x is a column vector and y is a row vector
        for i in range(mx):
            dot += x[i][0] * y[0][i]
    else: # x is a row vector and y is a column vector
        for i in range(nx):
            dot += x[0][i] * y[i][0]

    return dot

x = np.array([[1]])
y = np.array([[-1]])
# print(dot(x,y))