import numpy as np
from gauss_jordan_elimination import gauss_jordan_elimination

def matrix_inverse(A):
    if len(A.shape) != 2 or A.shape[0] != A.shape[1]:
        return "FAILED"
    identity = np.identity(A.shape[0])

    return gauss_jordan_elimination(A, identity)

# A = np.array([[-2,2,-5], [2,-3,7], [-4,3,-7]])
# A = np.array([[3,2,9], [-3,-3,-14], [3,1,3]])
# A = np.array([[2,-3,4], [2,-2,3], [6,-7,9]])
A = np.array([[-1,-4,-2], [2,6,2], [-1,0,3]])
print(matrix_inverse(A))