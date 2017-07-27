def arrayChange(inputArray):
	"""
	Input: an array of integers.

	On each move we are allowed to increase exactly one of its elements by one. 
	
	This finds the minimal number of moves required to obtain a strictly 
	increasing sequence from the input.
	"""
	
	moves = 0
	for i in range(0, len(inputArray)-1):
		while inputArray[i] >= inputArray[i+1]:
			difference = inputArray[i]-inputArray[i+1]+1
			inputArray[i+1] += difference
			moves += difference
	return moves

