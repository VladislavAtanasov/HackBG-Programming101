def sum_of_divisors(n):
	suma=0
	for i in range(1,n):
		if n%i==0:
			suma+=i
	return suma + n
print(sum_of_divisors(8))
print(sum_of_divisors(7))
print(sum_of_divisors(1))
print(sum_of_divisors(1000))