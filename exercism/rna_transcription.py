import re

def to_rna(strand):
	"""
	Given a DNA strand, returns its RNA complement 
	(per RNA transcription: G -> C, C -> G, T -> A, A -> U).

	strand (str): the DNA sequence to be translated

	Returns the transcripted RNA strand (str).
	"""

	transcription = str.maketrans("GCTA", "CGAU")
	invalid = re.compile('[^ATCG]')
	if invalid.search(strand.upper()):
		return ''
	return strand.upper().translate(transcription)
