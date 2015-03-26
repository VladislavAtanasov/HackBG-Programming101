def is_decreasing(seq):
	for a in range(0,len(seq)):
		if len(seq)==1:
			return True
		elif seq[a-1]>seq[a]:
			next
		elif seq[len(seq)-2]>seq[len(seq)-1]:
			return True
		else :
			return False
print(is_decreasing([5,4,3,2,1]))
print(is_decreasing([1,2,3]))
print(is_decreasing([100, 50, 20]))
print(is_decreasing([1,1,1,1]))