import numpy as np

def zerov(m):
    if len(m.shape) == 1:
        rows = 1
        columns = m.shape[0]
    else:
        rows = m.shape[0]
        columns = m.shape[1]
    for i in range(rows):
        for j in range(columns):
            m[i][j] = 0
    return m

# print(zerov(np.array([[3,1,1],[2,1,1]])))