def is_prime(n):
	if n==1 or n<0:
		return False
	else:
		for i in range(2,n):
			if n%i==0:
				return False
		return True
print(is_prime(1))
print(is_prime(2))
print(is_prime(8))
print(is_prime(11))
print(is_prime(-10))