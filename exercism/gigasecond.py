from datetime import datetime, timedelta

def add_gigasecond(birthday):
	"""
	This calculates when someone has lived for 10^9 seconds = 1 gigasecond.

	Input: birth date (datetime object) 

	Output: the date when someone has lived for a gigasecond (datetime object)
	"""

	gigasecond = (birthday + timedelta(seconds = 10**9))
	return gigasecond