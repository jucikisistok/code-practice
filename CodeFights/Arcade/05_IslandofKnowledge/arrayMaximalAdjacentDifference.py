def arrayMaximalAdjacentDifference(inputArray):
	"""
	Given an array of integers, this finds the maximal absolute difference between 
	any two of its adjacent elements.
	"""

	return max([abs(inputArray[i]-inputArray[i+1]) for i in range(len(inputArray)-1)])