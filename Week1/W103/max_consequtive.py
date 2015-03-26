def same(arr):
    start = 1
    end = len(arr)
    first = arr[0]
    result = [first]
    while start < end and arr[start] == first:
        result.append(arr[start])
        start+=1
    return result
def max_consecutive(items):
    start = 0
    end = len(items)
    count = []
    while len(items)!=0:
        current = len(same(items))
        items = items[len(same(items)):]
        count.append(current)
    return max(count)
print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))
print(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))
