import math

def nonprime(n=0):
	while 1:
		if n == 0:
			yield 1
		else:
			q = 1
			d = 2
			qq = math.sqrt(n + 1)
			while d <= qq:
				if (n + 1) % d == 0:
					q = 0
					break
				d += 1
			if not q:
				yield n + 1
		n += 1
