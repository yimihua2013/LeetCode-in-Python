
### LeetCode Excercise ###
'''
Excel Sheet Column Title
Given a positive integer, return its corresponding column title as appear in an Excel sheet.
For example:
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
'''
def convertToTitle(num):
	result = ''
	while num > 0:
	    result = chr(ord('A')+(num-1)%26)+result
	    num = (num-1)/26 
	return result


input = raw_input("input a integer: ")
number = int(input)
print convertToTitle(number)

