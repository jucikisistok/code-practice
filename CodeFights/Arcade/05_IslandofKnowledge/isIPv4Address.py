def isIPv4Address(inputString):
	"""
	Given a string, this finds out if it satisfies the IPv4 address naming rules.

	IPv4 addresses are represented in dot-decimal notation, which consists of four decimal numbers, 
	each ranging from 0 to 255, separated by dots, e.g., 172.16.254.1.
	"""
	
	numbers = inputString.split(".")

	in_range = [number for number in numbers if number.isnumeric() and len(numbers) == 4 and 0 <= int(number) <= 255]

	return len(numbers) == len(in_range)
