import numpy as np

def forward_substitution(A, b):
    if len(A.shape) != 2 or len(b.shape) != 2:
        return "FAILED"
    if A.shape[0] != A.shape[1]:
        return "FAILED"
    if b.shape[0] != A.shape[0] or b.shape[1] != 1:
        return "FAILED"
    
    for i in range(A.shape[0]):
        b[i+1:,0] -= b[i,0] * A[i+1:,i]

    return b