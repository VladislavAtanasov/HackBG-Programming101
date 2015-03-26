from copy import deepcopy
from pprint import pprint

def sum_matrix(m):
    return sum([sum(x) for x in m])

def calc_bombed_matrix(m, i, j):
    indexes = [-1, 0, 1]
    bombed_m = deepcopy(m)

    for row in indexes:
        for col in indexes:
            if i + row >= 0 and i + row<= len(bombed_m) - 1 and j + col >= 0 and j + col<= len(bombed_m[0]) - 1:
                if not(i + row == i and j + col == j):
                    if bombed_m[i][j] <= bombed_m[i + row][j + col]:
                        bombed_m[i+ row][j + col] -= bombed_m[i][j]
                    else:
                        bombed_m[i+ row][j + col] = 0

    return bombed_m

def matrix_bombing_plan(m):
    elements = {}

    for i in range(len(m)):
        for j in range(len(m[0])):
            total_sum = sum_matrix(calc_bombed_matrix(m, i, j))
            elements[(i, j)] = total_sum

    return elements

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
pprint(matrix_bombing_plan(m))