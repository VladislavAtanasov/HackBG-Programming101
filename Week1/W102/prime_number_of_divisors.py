def is_prime(n):
	if n==1 or n<0:
		return False
	else:
		for i in range(2,n):
			if n%i==0:
				return False
		return True
def sum_of_divisors(n):
	suma=0
	for i in range(1,n):
		if n%i==0:
			suma+=i
	return suma + n
def prime_number_of_divisors(x):
	if is_prime(sum_of_divisors(x)):
		return True
	else:
		return False
print(prime_number_of_divisors(7))
print(prime_number_of_divisors(8))
print(prime_number_of_divisors(9))
		