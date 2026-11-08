def sortedseq(seq):
	b = []
	for i in seq:
		if i != 0:
			b.append(i)
		else:
			if len(b) > 0:
				b = sorted(b)
				yield from b
				b = []
			yield 0
	if len(b) > 0:
		b = sorted(b)
		yield from b
		b = []
