def count_substrings(haystack,needle):
	new = haystack.count(needle)
	return new

	
print(count_substrings("This is a test string", "is"))
print(count_substrings("babababa", "baba"))
print(count_substrings("Python is an awesome language to program in!", "o"))
print(count_substrings("We have nothing in common!", "really?"))
print(count_substrings("This is this and that is this", "this"))