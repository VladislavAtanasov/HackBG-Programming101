def fac(n):
	if n==1 or n==0:
		return 1
	else:
		return n* fac(n-1)
def fact_digits(x):
	var=str(x)
	suma=0
	for i in var:
		suma+=fac(int(i))
	return suma
print(fact_digits(12))