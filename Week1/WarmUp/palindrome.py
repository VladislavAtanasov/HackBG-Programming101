def palindrome(obj):
	new=str(obj)
	if new[::-1] == new:
		return True
	else :
		return False
print(palindrome(121))
print(palindrome("kapak"))
print(palindrome("baba"))
