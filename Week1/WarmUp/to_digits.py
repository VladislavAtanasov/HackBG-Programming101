def to_digits(n):
	new=str(n)
	result = []
	for i in new:
		result.append(int(i))
	return result
print(to_digits(123))
print(to_digits(99999))
print(to_digits(123023))