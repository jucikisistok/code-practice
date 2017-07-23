from collections import Counter

def commonCharacterCount(s1, s2):
	"""
	Given two strings, this finds the number of common characters between them.
	"""

	cnt1 = Counter(s1)
	cnt2 = Counter(s2)

	common = 0
	for key in cnt1:
		common += (min(cnt1[key], cnt2[key]))
	return common