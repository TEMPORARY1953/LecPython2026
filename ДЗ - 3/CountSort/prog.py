c = []
for i in range(100):
	c.append([0] * 100)
while (s := input().strip()) != "":
	i, j = map(int, s.split(','))
	c[i - 1][j - 1] += 1
for i in range(100):
	for j in range(100):
		while c[i][j] > 0:
			print(f"{i + 1}, {j + 1}")
			c[i][j] -= 1
