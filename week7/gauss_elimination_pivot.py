import numpy as np

# A must be an n x (n+1) matrix / augmented matrix
def gauss_elimination_pivot(A):
    if len(A.shape) != 2:
        return "FAILED"
    if A.shape[0] != A.shape[1]:
        return "FAILED"
    
    p = np.zeros((A.shape[0], 1))

    for i in range(A.shape[0]-1):
        if A[i,i] == 0:
            # pivot
            for j in range(i+1, A.shape[0]):
                if A[j,i] != 0:
                    p[i,0] = j
                    tmp = A[i,:].copy()
                    A[i,:] = A[j,:]
                    A[j,:] = tmp
                    break
            if A[i,i] == 0: 
                # all 0s in current column => skip to next column
                continue
        else:
            p[i,0] = i
        A[i+1:,i] /= A[i,i]
        for j in range(i+1, A.shape[0]):
            for k in range(i+1, A.shape[0]):
                A[j][k] -= A[j][i] * A[i][k]
    return A, p

# A = np.array([[2,4,-2], [4,8,6], [-2,-4,5]])
# print(gauss_elimination_pivot(A))