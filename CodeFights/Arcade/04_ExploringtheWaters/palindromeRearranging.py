from collections import Counter

def palindromeRearranging(inputString):
	"""
	Given a string, this checks whether its characters can be rearranged to form a palindrome 
	(a string that reads the same left-to-right and right-to-left).
	"""

	c = Counter(inputString)

	return sum([1/inputString.count(letter) for letter in inputString if c[letter]%2 != 0]) <= 1