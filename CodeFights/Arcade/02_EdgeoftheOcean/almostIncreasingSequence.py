"""
Given a sequence of integers as an array, this determines whether it is 
possible to obtain a strictly increasing sequence by removing 
no more than one element from the array.
"""

def in_order(sequence):
	"""
	Takes the array and checks whether it's ordered or not.
	"""
	if all(x < y for x, y in zip(sequence, sequence[1:])):
		return -1

def bad_index(sequence):
	"""
	Retrieves the index corresponding to the element that is disrupting the order
	(the one larger than the subsequent element in the array).
	"""
	for i in range(len(sequence)-1):
		if sequence[i] >= sequence[i+1]:
			return i

def almostIncreasingSequence(sequence):
	"""
	Given the sequence and the index of the 'problematic' element, it checks whether 
	it is possible to obtain an increasing sequence by removing one element.
	"""
	ind = bad_index(sequence)

	#dropping the first element
	if in_order(sequence[1:]) == -1: 
		return True

	#dropping the element preceding the one with the bad_index
	if in_order(sequence[:ind-1] + sequence[ind:]) == -1:
		return True

	#dropping the element following the one with the bad_index
	if in_order(sequence[:ind+1] + sequence[ind+2:]) == -1: 
		return True

	#dropping the element with the bad_index
	if in_order(sequence[:ind] + sequence[ind+1:]) == -1: 
		return True

	return False