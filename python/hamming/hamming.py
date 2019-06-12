def distance(strand_a, strand_b):
	if len(strand_a) != len(strand_b):
		raise ValueError("strands are different lengths")

	hamming = [x for x in range(0, len(strand_a)) if strand_a[x] != strand_b[x]]

	return len(hamming)