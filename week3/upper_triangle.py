from zerov import zerov
import numpy as np

def upper_triangle(A):
    # check that A is n x n matrix
    if len(A.shape) < 2 or A.shape[0] != A.shape[1]:
        return "FAILED"

    for i in range(A.shape[0]):
        A[i+1:,i] = zerov(np.array([A[i+1:,i]]))
    
    return A

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(upper_triangle(A))