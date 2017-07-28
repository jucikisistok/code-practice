def adjacentElementsProduct(inputArray):
	"""
	Given an array of integers, it finds the pair of adjacent elements 
	that has the largest product and returns that product.
	"""

    return max([inputArray[i] * inputArray[i + 1] for i in range(len(inputArray) - 1)])