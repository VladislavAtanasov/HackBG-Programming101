def contains_digit(number,digit):
	for x in str(number):
		if digit == int(x):
			return True
	return False
def contains_digits(number,digits):
	for x in digits:
		if contains_digit(number,x)==False:
			return False
	return True
print(contains_digits(402123, [0, 3, 4]))
print(contains_digits(666, [6,4]))
print(contains_digits(123456789, [1,2,3,0]))
print(contains_digits(456, []))