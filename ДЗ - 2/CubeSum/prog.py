import math

N = int(input())
A = 1
B = int(math.floor(N ** (1/3)))
c = 0
while A <= B:
	s = A**3 + B**3
	if s == N:
		c += 1
		A += 1
		B -= 1
	elif s < N:
		A += 1
	else:
		B -= 1
print(c)
