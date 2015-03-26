def reduce_file_path(path):
    first = ".."
    second = "."
    third = "/"
    if path == third or path.count(third) == len(path):
        return third
    elif second not in path and first not in path:
        for i in range(1,len(path)):
            if path[i - 1] == "/" and path[i] == "/" and path[len(path) - 1] == third:
                return path[:i] + path[i+1:len(path)-1]
            elif path[i - 1] == "/" and path[i] == "/" and path[len(path) - 1] != third:
                return path[:i] + path[i+1:]
        if path[len(path) - 1] == third:
            return path[:len(path)-1]
        else:
            return path
    elif first in path:
        return path[:path.index(first) - 4]
    elif second in path:
        return path[:path.index(second) - 1]


print(reduce_file_path("/"))
print(reduce_file_path("/srv/../"))
print(reduce_file_path("/srv/www/htdocs/wtf/"))
print(reduce_file_path("/srv/www/htdocs/wtf"))
print(reduce_file_path("/srv/./././././"))
print(reduce_file_path("/etc//wtf/"))
print(reduce_file_path("/etc/../etc/../etc/../"))
print(reduce_file_path("//////////////"))
print(reduce_file_path("/../"))
