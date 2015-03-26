def count_words(arr):
	diction = {}
	for key in arr:
		diction[key] = arr.count(key)
	return diction
print(count_words(["apple", "banana", "apple", "pie"]))
print(count_words(["python", "python", "python", "ruby"]))