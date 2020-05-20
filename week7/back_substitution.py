import numpy as np

def back_substitution(A, b):
    if len(A.shape) != 2 or len(b.shape) != 2:
        return "FAILED"
    if A.shape[0] != A.shape[1]:
        return "FAILED"
    if b.shape[0] != A.shape[0] or b.shape[1] != 1:
        return "FAILED"

    for i in range(A.shape[0]-1, -1, -1):
        div = b[i,0]
        for j in range(i+1, A.shape[0]):
            div -= A[i,j] * b[j,0]
        b[i,0] = div / A[i,i]
        
    return b