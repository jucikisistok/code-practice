def matrixElementsSum(matrix):
	"""
	After becoming famous, CodeBots decided to move to a new building and live together. 
	The building is represented by a rectangular matrix of rooms, each cell containing an 
	integer - the price of the room. Some rooms are free (their cost is 0), but that's 
	probably because they are haunted, so all the bots are afraid of them. That is why 
	any room that is free or is located anywhere below a free room in the same column is 
	not considered suitable for the bots.

	Help the bots calculate the total price of all the rooms that are suitable for them.
	"""
	
	total_price = 0
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):     
			if i < len(matrix)-1 and matrix[i][j] == 0:
				#we don't need to look at the last row since
				#there is nothing below
				matrix[i + 1][j] = 0
			total_price = total_price + matrix[i][j]
	return total_price

