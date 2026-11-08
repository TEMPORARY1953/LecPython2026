def joinseq(*seqs):
	its = []
	for s in seqs:
		its.append(iter(s))
	h = []
	for it in its:
		h.append(next(it, None))
	while 1:
		bi = -1
		for i in range(len(h)):
			if h[i] is None:
				continue
			if bi == -1 or h[i] < h[bi]:
				bi = i
		if bi == -1:
			break
		yield h[bi]
		h[bi] = next(its[bi], None)
