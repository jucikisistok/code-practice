from collections import Counter

def areSimilar(a, b):
	"""
	Two arrays are called similar if one can be obtained from another 
	by swapping at most one pair of elements in one of the arrays.

	Given two arrays a and b, this checks whether they are similar.
	"""
	
	if Counter(a) == Counter(b):
		#only checking pairs of arrays that have the same
		#composition of elements, can't be true otherwise
		if sum(i != j for i, j in zip(a, b)) <= 2:
			return True
	return False
