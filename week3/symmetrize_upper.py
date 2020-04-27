import numpy as np

# makes the bottom half symmetrical to the top half
def symmetrize_upper(A):
    # check that A is n x n matrix
    if len(A.shape) < 2 or A.shape[0] != A.shape[1]:
        return "FAILED"

    for i in range(1, A.shape[0]):
        A[i,:i] = A[:i,i]

    return A

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(symmetrize_upper(A))