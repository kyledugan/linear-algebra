import numpy as np
from zerov import zerov

def identity(x):
    # check that A is n x n matrix
    if len(x.shape) < 2 or x.shape[0] != x.shape[1]:
        return "FAILED"
    for i in range(x.shape[0]):
        x[:i, i] = zerov(np.array([x[:i, i]])) #a01
        x[i, i] = 1 #a11
        x[i+1:, i] = zerov(np.array([x[i+1:, i]])) #a12
    return x

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(identity(arr))