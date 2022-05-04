#!/usr/bin/python

def int_reverse(integer):
	if (isinstance(integer, int)):
		reversed = 0
		remainder = 0
		
		temp = abs(integer)
		
		while temp > 0:
			remainder = temp % 10
			temp = temp//10
			reversed = reversed * 10 + remainder
		
		if integer < 0:
			return (-reversed)
			
		return (reversed)
	
	return ("Wrong Input!")
	

if __name__ == '__main__':
	print (int_reverse(-773))