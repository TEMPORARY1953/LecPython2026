pr = set()
nb = set()
while True:
	try:
		line = input().strip()
	except EOFError:
		break
	if line == "":
		break
	parts = line.split(",")
	m = int(parts[0].strip())
	n = int(parts[1].strip())
	if m == 0 and n == 0:
		break
	if m == n:
		continue
	nb.add(m)
	nb.add(n)
	pr.add((m, n))
	pr.add((n, m))
sortpr = sorted(pr)
q = -1
c = 0
final = []
for i in range(len(sortpr)):
	if sortpr[i][0] != q:
		if c == len(nb) - 1:
			final.append(q)
		q = sortpr[i][0]
		c = 1
	else:
		c += 1
if c == len(nb) - 1 and q != -1:
	final.append(q)
print(" ".join(map(str, final)))
