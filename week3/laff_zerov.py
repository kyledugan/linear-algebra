import numpy as np

def laff_zerov(m):
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            m[i][j] = 0
    return m

print(laff_zerov(np.array([[3,1,1],[2,1,1]])))