def is_increasing(seq):
	for a in range(0,len(seq)):
		if len(seq)==1:
			return True
		elif seq[a-1]<seq[a]:
			next
		elif seq[len(seq)-2]<seq[len(seq)-1]:
			return True
		else :
			return False
print(is_increasing([1,2,3,4,5]))
print(is_increasing([1]))
print(is_increasing([5,6,-10]))
print(is_increasing([1,1,1,1]))