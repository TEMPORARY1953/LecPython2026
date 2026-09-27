s1 = input().strip()
c = 0
while (s2 := input().strip()) != "":
	for i in range(len(s1) - 1):
		if s1[i] == '#' and s1[i + 1] == '.' and s2[i] == '.' and s2[i + 1] == '.':
			c += 1
	if s1[len(s1) - 1] == '#' and s2[len(s1) - 1] == '.':
		c += 1
	s1 = s2
for i in range(len(s1) - 1):
	if s1[i] == '#' and s1[i + 1] == '.':
		c += 1
if s1[len(s1) - 1] == '#':
	c += 1
print(c)
