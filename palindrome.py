#!/usr/bin/python

def is_palindrome(string):
	if string:
		string = str(string)
		low = 0
		high = len(string)-1
		if string[high].lower() != string[low].lower():
			return (False)
		
		while high > low:
			if string[high].lower() != string[low].lower():
				return (False)
			low += 1
			high -= 1
		return (True)
	return (False)

	# Easy pythonic way
#	string = str(string)
#	return (string.lower() == string[::-1].lower())
			
			
if __name__ == '__main__':
	string = 'madam'
	a = is_palindrome(string)
	print a
		