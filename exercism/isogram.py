def is_isogram(word):
	"""
	Determines if a word or phrase is an isogram
	(a word / phrase without a repeating letter.)

	Takes a word (str) and returns True if it's an isogram, False otherwise.
	"""

	word = [char for char in word.lower() if char.isalpha()]
	for character in word:
		if word.count(character) > 1:
			return False
	return True