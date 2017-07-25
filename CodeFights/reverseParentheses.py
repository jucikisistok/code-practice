def reverseParentheses(s):
	"""
	Input: a string s that consists of English letters, punctuation marks, 
	whitespace characters, and brackets. It is guaranteed that the parentheses 
	in s form a regular bracket sequence.

	This reverses the strings contained in each pair of matching parentheses, 
	starting from the innermost pair. The results string doesn't contain 
	any parentheses.
	"""

	while s.find("(") != -1:
		opening = s.rfind("(")
		closing = s.find(")", opening)
		in_parentheses = "".join(reversed(s[opening+1:closing]))
		s = s[0:opening] + in_parentheses + s[closing+1:]

	return s


