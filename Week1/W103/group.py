def same(arr):
    start = 1
    end = len(arr)
    first = arr[0]
    result = [first]
    while start < end and arr[start] == first:
        result.append(arr[start])
        start+=1
    return result
def group(arr):
    start = 0
    end = len(arr)
    result = []
    new=[]
    while len(arr)!=0:
        group = same(arr)
        result.append(group)
        arr=arr[len(group):]
    return result

print(group([1, 1, 1, 2, 3, 1, 1]))
print(group([1, 2, 1, 2, 3, 3]))
