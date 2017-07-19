def checkPalindrome(inputString):
	"""
	Given a string, it checks if the string is a palindrome.

	A palindrome is a word, phrase, or sequence that reads the same backwards as forwards.
	"""

    if inputString == inputString[::-1]:
        return True
    return False