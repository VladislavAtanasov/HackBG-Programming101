def unique_words_count(arr):
	newarr = []
	count = 0
	for item in arr:
		if item not in newarr:
			newarr.append(item) 
			count+=1
	return count
print(unique_words_count(["apple", "banana", "apple", "pie"]))
print(unique_words_count(["python", "python", "python", "ruby"]))
print(unique_words_count(["HELLO!"] * 10))