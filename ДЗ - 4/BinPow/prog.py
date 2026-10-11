def BinPow(a, n, f):
	res = a
	q = a
	n -= 1
	while n > 0:
		if n % 2 != 0:
			res = f(res, q)
		q = f(q, q)
		n //= 2
	return res
