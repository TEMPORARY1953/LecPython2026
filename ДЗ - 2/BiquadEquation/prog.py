import math

a, b, c = map(float, input().split(','))
x = []

if math.isclose(a, 0):
	if math.isclose(b, 0):
		if math.isclose(c, 0):
			print(-1)
		else:
			print(0)
	else:
		if math.isclose(c, 0):
			print(0.0)
		elif c*b > 0:
			print(0)
		else:
			x.append(math.sqrt(-1 * c/b))
			x.append(-1 * math.sqrt(-1 * c/b))
			un = sorted(set(x))
			print(*un)
else:
	D = b*b - 4*a*c
	if D < 0 and not math.isclose(D, 0):
		print(0)
	elif math.isclose(D, 0):
		q = -1 * b / (2*a)
		if q < 0 and not math.isclose(q, 0):
			print(0)
		elif math.isclose(q, 0):
			print(0.0)
		else:
			x.append(math.sqrt(q))
			x.append(-1 * math.sqrt(q))
			un = sorted(set(x))
			print(*un)
	else:
		q1 = ((-1 * b) +  math.sqrt(D))/ (2*a)
		q2 = ((-1 * b) -  math.sqrt(D))/ (2*a)
		if q1 >= 0:
			if math.isclose(q1, 0):
				x.append(0.0)
			else:
				x.append(math.sqrt(q1))
				x.append(-math.sqrt(q1))
		if q2 >= 0:
			if math.isclose(q2, 0):
				x.append(0.0)
			else:
				x.append(math.sqrt(q2))
				x.append(-math.sqrt(q2))
		un = sorted(set(x))
		if not un:
			print(0)
		else:
			print(*un)
