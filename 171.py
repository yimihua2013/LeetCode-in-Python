
### (No. 171)Excel Sheet Column Number ###
'''
Given a column title as appear in an Excel sheet, return its corresponding column number.
For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
'''

def titleToNumber(s):
	lex = len(s)
	if lex > 0:
		num = 0

        for i in range(lex):
            num += ((ord(s[i])%65)+1)*(26**(lex-i-1))
        return num 



title = raw_input("input an Excel colnum title(like 'A','AB','AAB'): ")
print titleToNumber(title)