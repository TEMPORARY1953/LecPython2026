import random
def divrandom(a, b, s, p):
	if a > b:
		b, a = a, b
	if a % p == 0 and s % p == 0:
		return 0
	n = (b - a) // s + 1
	q = 1
	while q == 1:
		k = random.randrange(n)
		x = a + k * s
		if x % p != 0:
			return x
