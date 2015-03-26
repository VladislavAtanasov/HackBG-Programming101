def next_hack(n):
	for x in range(n+1,100000):
		new = str(bin(x).replace("0b",""))
		counter=0
		for i in new:
			if i == "1":
		 		counter+=1
		if new == new[::-1] and counter%2!=0:
			return x
			break
print(next_hack(0))
print(next_hack(10))
print(next_hack(8031))