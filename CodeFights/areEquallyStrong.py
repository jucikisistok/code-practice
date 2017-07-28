from collections import Counter

def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
	"""
	Call two arms equally strong if the heaviest weights they each are able to lift are equal.

	Call two people equally strong if their strongest arms are equally strong (the strongest arm 
	can be both the right and the left), and so are their weakest arms.

	Given your and your friend's arms' lifting capabilities this finds out if you two are equally strong.
	"""

	you = [yourLeft, yourRight]
	friend = [friendsLeft, friendsRight]

	return Counter(you) == Counter(friend)

print(areEquallyStrong(10,15,15,10), "should be true")
print(areEquallyStrong(15,10,15,10), "should be true")
print(areEquallyStrong(15,10,15,9), "should be true")