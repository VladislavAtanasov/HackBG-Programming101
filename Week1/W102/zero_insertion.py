def to_number(digits):
	number=""
	for i in digits:
		number+=str(i)
	return int(number)
def zero_insert(n):
	new=[]
	result = []
	for x in str(n):
		result.append(int(x))
	start = 0
	end = len(result)
	while start<end - 1:
		x=result[start]
		y=result[start+1]
		new.append(x)
		if (x+y)%10==0 or x==y:
			new.append(0)
		start+=1
	new.append(result[start])
	return to_number(new)
print(zero_insert(116457))
print(zero_insert(55555555)) 
print(zero_insert(1))
print(zero_insert(6446))