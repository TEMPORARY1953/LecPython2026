seq = set(eval(input()))

if not seq:
	print(0)
else:
	mx = max(seq)
	mxrut = int(mx ** 0.5) + 1
	s = []
	for i in range(1, mxrut + 1):
		s.append(i * i)
	sums = set()
	for i in range(len(s)):
		if s[i] * 3 > mx:
			break
		for j in range(i, len(s)):
			s[j]
			if s[i] + s[j] * 2 > mx:
				break
			for k in range(j, len(s)):
				if s[i] + s[j] + s[k] > mx:
					break
				sums.add(s[i] + s[j] + s[k])
	print(len(seq & sums))
