def is_number_balanced(n):
	mine=str(n)
	if len(mine)==1:
		return True
	else:
		new=[]
		for x in mine:
			new.append(int(x))
		if len(mine)==2:
			if new[0]==new[1]:
				return True
			else:
				return False
		else:		
			if len(mine)%2!=0:
				result1 = sum([new[x] for x in range(0, len(new)/2)])
				result2 = sum([new[a] for a in range((len(new)/2) +1,len(new))])
				
				if result1==result2:
					return True
				else:
					return False
			elif len(mine)%2==0:
				result1 = sum([new[x] for x in range(0, len(new)/2)])
				result2 = sum([new[a] for a in range(len(new)/2,len(new))])
				
				if result1==result2:
					return True
				else:
					return False
	#mine=str(n)
	#new1= sum([int(x) for x in range(1,len(mine)//2)])
	#new2= sum([int(x) for x in range((len(mine)//2)+1,len(mine)+1)])
	#if len(mine)==1:
	#	return True
	#elif new1==new2:
	#	return True
	#else:
	#	return False
print(is_number_balanced(9))
print(is_number_balanced(11))
print(is_number_balanced(13))
print(is_number_balanced(121))
print(is_number_balanced(4518))
print(is_number_balanced(28471))
print(is_number_balanced(1238033))