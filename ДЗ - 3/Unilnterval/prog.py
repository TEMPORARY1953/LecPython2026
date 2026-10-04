i = []
s = input()
for p in s.split("),"):
	a, b = p.strip("( )").split(",")
	i.append([int(a), int(b)])
i.sort()
fin = []
for j in range(len(i)):
	if not fin or fin[-1][1] < i[j][0]:
		fin.append(i[j])
	else:
		if i[j][1] > fin[-1][1]:
			fin[-1][1] = i[j][1]
sm = 0
for j in range(len(fin)):
	sm += fin[j][1] - fin[j][0]
print(sm)
