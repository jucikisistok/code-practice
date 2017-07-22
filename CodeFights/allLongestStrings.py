def allLongestStrings(inputArray):
	"""
	Given an array of strings, it returns another array 
	containing all of its longest strings.
	"""

    max_length = max(len(element) for element in inputArray)
     
    return [element for element in inputArray if len(element) == max_length]