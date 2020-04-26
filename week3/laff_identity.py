import numpy as np
from laff_zerov import laff_zerov

def laff_identity(x):
    if len(x.shape) < 2:
        return "FAILED"
    if x.shape[0] != x.shape[1]:
        return "FAILED"
    for i in range(x.shape[0]):
        x[:i, i] = laff_zerov(np.array([x[:i, i]])) #a01
        x[i, i] = 1 #a11
        x[i+1:, i] = laff_zerov(np.array([x[i+1:, i]])) #a12
    return x

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(laff_identity(arr))