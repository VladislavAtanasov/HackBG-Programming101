def prepare_meal(number):
    string = "''"
    if number % 3 == 0 and number % 5 == 0:
        new = max([n for n in range(number) if (3**n)*5 == number])
        return "spam " * new + "and eggs"
    elif number % 5 == 0:
        return "eggs"
    elif number%3 == 0:
        new = max([n for n in range(number) if 3**n == number])
        return "spam "*new
    else:
        return string


print(prepare_meal(3))
print(prepare_meal(27))
print(prepare_meal(7))
print(prepare_meal(5))
print(prepare_meal(15))
print(prepare_meal(45))

