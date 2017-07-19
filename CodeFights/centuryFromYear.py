def centuryFromYear(year):
	"""
	Given a year, return the century it is in. 

	The first century spans from the year 1 up to and including the year 100,
	the second - from the year 101 up to and including the year 200, etc.

	"""
    if year%100 == 0:
        century = int(year/100) 
    else:
        century = int(year/100 + 1)
    return century