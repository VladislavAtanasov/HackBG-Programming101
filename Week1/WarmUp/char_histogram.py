def char_histogram(string):
	diction={}
	count=0
	for i in string:
		if i in diction:
			count+=1
			diction[i]=count
		elif i not in diction:
			count=1
			diction[i]=count
	return diction
print(char_histogram("Python!"))
print(char_histogram("AAAAaaa!!!"))