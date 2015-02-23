
### No.7: Reverse digits of an integer.###
'''
Example1: x = 123, return 321
Example2: x = -123, return -321

Have you thought about this?
_Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!
_If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.
_Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?
_For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

def reverse(num):
	if num >0:
		sign = 1
	else:
		sign = -1
	
	num_new = str(abs(num))
	rev_num = int(num_new[::-1])

	if rev_num < 2**31:
		return sign*rev_num
	else:
		return 0

print reverse(123)
print reverse(12300)
print reverse(1000000003) # overflow case
