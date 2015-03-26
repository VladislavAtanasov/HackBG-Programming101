def is_an_bn(word):
    n = word.count("a")
    m = word.count("b")
    if word == "":
        return True
    elif n==m and word == "a"*n + "b"*m:
        return True
    else:
        return False

print(is_an_bn(""))
print(is_an_bn("rado"))
print(is_an_bn("aaabb"))
print(is_an_bn("aaabbb"))
print(is_an_bn("aabbaabb"))
print(is_an_bn("bbbaaa"))
print(is_an_bn("aaaaabbbbb"))
