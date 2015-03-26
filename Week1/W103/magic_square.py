def same(arr):
    start = 1
    end = len(arr)
    first = arr[0]
    result = [first]
    while start < end and arr[start] == first:
        result.append(arr[start])
        start+=1
    return result
def magic_square(matrix):
    new1 = [sum(row) for row in matrix]
    new2 = [sum(row[col] for row in matrix) for col in range(len(matrix[0]))]
    new3 = sum([matrix[row][col] for row in range(len(matrix)) for col in range(len(matrix[0])) if col == row ])
    new4 = sum([matrix[row][col] for row in range(len(matrix)) for col in range(len(matrix[0])) if len(matrix[0]) - (col + row) == 1])
    if len(same(new1)) == len(new1) and len(same(new2)) == len(new2) and new3 in new2 and new4 in new2:
        return True
    else:
        return False

print(magic_square([[1,2,3], [4,5,6], [7,8,9]]))
print(magic_square([[4,9,2], [3,5,7], [8,1,6]]))
print(magic_square([[7,12,1,14], [2,13,8,11], [16,3,10,5], [9,6,15,4]]))
print(magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))
print(magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]]))
