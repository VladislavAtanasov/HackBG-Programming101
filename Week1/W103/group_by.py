def groupby(func, seq):
    result = {}

    for item in seq:
        if func(item) not in result:
            result[func(item)] = [item]
        elif func(item) in result:
            result[func(item)].append(item)

    return result

print(groupby(lambda x: x % 2, [0,1,2,3,4,5,6,7]))
print(groupby(lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12]))
print(groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7]))
