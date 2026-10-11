def pattsort(pattern, seq):
	pattern = sorted(range(len(pattern)), key=lambda i: pattern[i])
	sort_seq = sorted(seq)
	res = [0] * len(seq)
	for i in range(len(seq)):
		res[pattern[i]] = sort_seq[i]
	return res
