import numpy as np
from gaussian_elimination import gaussian_elimination
from forward_substitution import forward_substitution
from back_substitution import back_substitution

def solve_Ax_eq_b(A, b):
    A = gaussian_elimination(A)
    b = forward_substitution(A, b)
    return back_substitution(A, b)

A = np.array([[2,0,1,2], [-2,-1,1,-1], [4,-1,5,4], [-4,1,-3,-8]])
b = np.array([[2],[2],[11],[-3]])
print(solve_Ax_eq_b(A, b))

    