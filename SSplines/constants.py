import numpy as np

PS12_BARYCENTRIC_COORDINATES = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [0.5, 0.5, 0],
    [0, 0.5, 0.5],
    [0.5, 0, 0.5],
    [0.5, 0.25, 0.25],
    [0.25, 0.5, 0.25],
    [0.25, 0.25, 0.5],
    [1 / 3, 1 / 3, 1 / 3]
])

PS12_SUB_TRIANGLE_VERTICES = np.array([
    [0, 3, 6],
    [3, 1, 7],
    [1, 4, 7],
    [4, 2, 8],
    [2, 5, 8],
    [5, 0, 6],
    [6, 3, 9],
    [3, 7, 9],
    [4, 8, 9],
    [5, 9, 8],
    [5, 6, 9]
], dtype=np.int)