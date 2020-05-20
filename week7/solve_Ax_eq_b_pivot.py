import numpy as np
from gauss_elimination_pivot import gauss_elimination_pivot
from forward_substitution_pivot import forward_substitution_pivot
from back_substitution import back_substitution

def solve_Ax_eq_b(A, b):
    A, p = gauss_elimination_pivot(A)
    b = forward_substitution_pivot(A, b, p)
    return back_substitution(A, b)

# A = np.array([[2,-4,-2], [4,8,6], [6,-4,2]], dtype=float)
# b = np.array([[2], [0], [1]], dtype=float)
A = np.array([[0.02, 0.01, 0, 0], [1, 2, 1, 0], [0, 1, 2, 1], [0, 0, 100, 200]], dtype=float)
b = np.array([[0.02], [1], [4], [800]], dtype=float)
print(solve_Ax_eq_b(A, b))

    