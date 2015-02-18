 ### No. 169_Majority Element###
'''
  Given an array of size n, find the majority element. 
  The majority element is the element that appears more than [n/2] times.
  You may assume that the array is non-empty and the majority element always exist in the array.
'''
# method 1(slow, failed to pass leetcode judgement)
def majorityElement(arr):
  	lex = len(arr)
  	if lex >0:
  		for item in arr:
  			times = arr.count(item)
  			if times > lex/2:
  		         return item

# method 2(this one passed)
def majorityElement2(arr):
  	lex = len(arr)
  	h = {}
  	for item in arr:
  		if h.has_key(item):
  			h[item] += 1
  		else:
  			h[item] = 1
        if h[item] > lex/2:
  	        return item
        
test = [1,3,4,1,5,1,1]
test2 = ['a','b','c','a','a']
print majorityElement(test)
print majorityElement(test2)
print majorityElement2(test)
print majorityElement2(test2)
