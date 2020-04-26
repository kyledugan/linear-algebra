from laff_zerov import laff_zerov
import numpy as np

def laff_upper_triangle(A):
    # check for 2D matrix
    if len(A.shape) < 2:
        return "FAILED"
    # check that A is n x n matrix
    if A.shape[0] != A.shape[1]:
        return "FAILED"

    for i in range(A.shape[0]):
        A[i+1:,i] = laff_zerov(np.array([A[i+1:,i]]))
    
    return A

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(laff_upper_triangle(A))