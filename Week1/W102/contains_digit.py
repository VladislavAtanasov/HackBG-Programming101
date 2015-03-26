def contains_digit(number,digit):
	for x in str(number):
		if digit == int(x):
			return True
	return False
print(contains_digit(123, 4))
print(contains_digit(42, 2))
print(contains_digit(1000, 0))
print(contains_digit(12346789, 5))