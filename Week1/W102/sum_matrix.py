def sum_matrix(m):
	return sum([sum(x) for x in m])
print(sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(sum_matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
print(sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))