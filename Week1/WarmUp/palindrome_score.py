def p_score(n):
	new=str(n)
	if new == new[::-1]:
		return 1
	else:
		return 1+p_score(int(new)+int(new[::-1]))
print(p_score(121))
print(p_score(48))
print(p_score(198))