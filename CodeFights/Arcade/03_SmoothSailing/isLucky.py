def isLucky(n):
	"""
	Ticket numbers usually consist of an even number of digits. A ticket number 
	is considered lucky if the sum of the first half of the digits is equal to 
	the sum of the second half.

	Given a ticket number n, this determines if it's lucky or not.
	"""

	num_str = str(n)
	half = int(len(num_str)/2)
	first_half = [int(num_str[i:i+1]) for i in range(0,half,1)]
	second_half = [int(num_str[i:i+1]) for i in range(half,len(num_str),1)]
	
	return sum(first_half) == sum(second_half)