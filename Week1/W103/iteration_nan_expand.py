def iterations_of_nan_expand(expanded):
    new = "Not a"
    if new in expanded.strip() and expanded.strip() == expanded:
        return expanded.count(new)
    elif expanded == "":
        return 0
    else:
        return False
print(iterations_of_nan_expand(""))
print(iterations_of_nan_expand("Not a NaN"))
print(iterations_of_nan_expand("Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN"))
print(iterations_of_nan_expand("Show these people!"))
