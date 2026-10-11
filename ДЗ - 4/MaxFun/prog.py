def maxfun(S, F1, *Fi):
	mxF = F1
	mxsm = 0
	for x in S:
		mxsm += F1(x)
	for F in Fi:
		s = 0
		for x in S:
			s += F(x)
		if s >= mxsm:
			mxF = F
			mxsm = s
	return mxF
