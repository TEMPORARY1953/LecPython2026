import itertools

def checkcomm(fun, *args):
	a1 = fun(*args)
	q = True
	for perm in itertools.permutations(args):
		if fun(*perm) != a1:
			q = False
	return q
