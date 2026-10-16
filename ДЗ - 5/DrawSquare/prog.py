def squares(w, h, *r):
	q = [['.'] * w for _ in range(h)]
	for (X, Y, s, c) in r:
		for y in range(Y, Y + s):
			for x in range(X, X + s):
				q[y][x] = c
	for i in q:
		print(''.join(i))
