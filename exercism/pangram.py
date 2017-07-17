import string

def is_pangram(sentence):
	"""
	Determines if a sentence is a pangram (a sentence using 
	every letter of the alphabet at least once).

	sentence (str): the sentence to be tested

	Returns True if it's a pangram, False otherwise.
	"""

	sentence = {character for character in sentence.lower() if character.isalpha()}
	alphabet = string.ascii_lowercase
	return len(alphabet) == len(sentence)