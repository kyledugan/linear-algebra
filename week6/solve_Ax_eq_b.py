import numpy as np
from gaussian_elimination import gaussian_elimination
from back_substitution import back_substitution

def solve_Ax_eq_b(A, b):
    A = gaussian_elimination(A)
    return back_substitution(A, b)

A = np.array([[2,0,1,2], [-2,-1,1,-1], [4,-1,5,4], [-4,1,-3,-8]])
b = np.array([[2],[2],[11],[-3]])
print(solve_Ax_eq_b(A, b))

    