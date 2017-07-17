import re

def word_count(phrase):
	""" 
	Given a phrase, counts the occurrences of each word in that phrase.
	"""

	phrase = re.sub('[^0-9a-zA-Z]+', ' ', phrase.lower())
	word_list = phrase.split()
	word_dict = dict([ (word, word_list.count(word)) for word in word_list ])
	
	return word_dict