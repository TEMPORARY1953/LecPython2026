import collections

lines1 = []
lines2 = []
q = 1
while True:
	try:
		line = input()
	except EOFError:
		break
	if line == "":
		break
	if q == 1:
		lines1.append(line)
		q = 2
	elif q == 2:
		lines2.append(line)
		q = 1
gl = []
for i in range(len(lines1)):
	gl.append(lines1[i][0])
for i in range(len(lines2)):
	gl.append(lines2[i][0])
gl = set(gl)
sl1 = set()
sl2 = set()
for i in range(len(lines1)):
	for c in lines1[i]:
		if c not in gl:
			sl1.add(c)
for i in range(len(lines2)):
	for c in lines2[i]:
		if c not in gl:
			sl2.add(c)
if len(sl1) > len(sl2):
	print("Mumbo")
else:
	print("Jumbo")
