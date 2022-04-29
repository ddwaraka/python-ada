#!/usr/bin/python

# O(n) way to reverse an array - udemy Section 5, lecture 12
def arr_rev(arr):
	low_index = 0
	high_index = len(arr)-1
	
	while high_index > low_index:
		# I didn't know we could swap variables likes this!
		arr[low_index], arr[high_index] = arr[high_index], arr[low_index]
		
		# For reference, using a temp variable - probably more memory efficient that python swapping
		# Python swapping uses a tuple to evaluate RHS first, maybe more memory than a variable
		
		# temp_variable = arr[low_index]
		# arr[low_index] = arr[high_index]
		# arr[high_index] = tem
		
		low_index += 1
		high_index -= 1
		
	
	return (arr)


if __name__ == '__main__':
	arr = [1,2,3,4]
	print arr_rev(arr)
		
	
	
		