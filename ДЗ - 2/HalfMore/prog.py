hm = None
c = 0
while (s := input().strip()) != "":
	a = eval(s)
	if c == 0:
		hm = a
		c += 1
	elif a == hm:
		c += 1
	else:
		c -= 1
print(hm)
