def count_consonants(str):
	count=0
	consonants="bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
	for i in str:
		if i in consonants:
			count+=1
	return count
print(count_consonants("Python"))
print(count_consonants("Theistareykjarbunga"))
print(count_consonants("grrrrgh!"))
print(count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))
print(count_consonants("A nice day to code!"))