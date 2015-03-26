def to_number(digits):
	number=""
	for i in digits:
		number+=str(i)
	return number
print(to_number([1,2,3]))
print(to_number([9,9,9,9,9]))
print(to_number([1,2,3,0,2,3]))