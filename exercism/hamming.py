def distance(strand1, strand2):
    """
    Calculates the Hamming distance (number of differences) between two DNA strands. 
    This gives us the minimum number of point mutations that could have occurred on 
    the evolutionary path between the two strands.

    strand1, strand2 (str): DNA strands to be compared

    Returns the Hamming distance (int).
    """

    if len(strand1) != len(strand2):
        raise ValueError("The two DNA strands must be of equal length!")

    hammingDist = 0
    for a, b in zip(strand1, strand2):
        if a != b:
            hammingDist += 1
    return hammingDist