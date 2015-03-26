def count_vowels(str):
	count=0
	vowels="aieouyAIEOUY"
	for i in str:
		if i in vowels:
			count+=1
	return count
print(count_vowels("Python"))
print(count_vowels("Theistareykjarbunga"))
print(count_vowels("grrrrgh!"))
print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))
print(count_vowels("A nice day to code!"))
