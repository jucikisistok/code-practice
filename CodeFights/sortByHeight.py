def sortByHeight(a):
	"""
	Some people are standing in a row in a park. There are trees 
	between them which cannot be moved. 

	If a[i] = -1, then the ith position is occupied by a tree. 
	Otherwise a[i] is the height of a person standing in the ith position.

	This rearranges the people by their heights in a non-descending 
	order without moving the trees.
	"""

	sorted_array = sorted([i for i in a if i != -1])
	
	for i in range(len(a)):
		if a[i] == -1:
			sorted_array.insert(i, -1)
	
	return sorted_array
