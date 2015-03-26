def nan_expand(times):
	new = ""
	if times == 0:
		return new
	else:
		for x in range(0,times):
			return "Not a "  * times + "Nan"
print(nan_expand(0))
print(nan_expand(1))
print(nan_expand(2))
print(nan_expand(3))
