d = []
line = input()
while line.strip() != "":
	xs, ys = line.split(",")
	x = int(xs.strip())
	y = int(ys.strip())
	d.append((x, y))
	line = input()
n = ((d[-1][0] - d[-2][0]) * (d[0][1] - d[-1][1])) - ((d[-1][1] - d[-2][1]) * (d[0][0] - d[-1][0]))
if n > 0:
	f = '+'
if n < 0:
	f = '-'
if n == 0:
	f = 'N'
if f == '+':
	for i in range(len(d) - 2):
		n = ((d[i + 1][0] - d[i][0]) * (d[i + 2][1] - d[i + 1][1])) - ((d[i + 1][1] - d[i][1]) * (d[i + 2][0] - d[i + 1][0]))
		if n <= 0:
			f = 'N'
			break
	n = ((d[0][0] - d[-1][0]) * (d[1][1] - d[0][1])) - ((d[0][1] - d[-1][1]) * (d[1][0] - d[0][0]))
	if n <= 0:
		f = 'N'
elif f == '-':
	for i in range(len(d) - 2):
		n = ((d[i + 1][0] - d[i][0]) * (d[i + 2][1] - d[i + 1][1])) - ((d[i + 1][1] - d[i][1]) * (d[i + 2][0] - d[i + 1][0]))
		if n >= 0:
			f = 'N'
			break
	n = ((d[0][0] - d[-1][0]) * (d[1][1] - d[0][1])) - ((d[0][1] - d[-1][1]) * (d[1][0] - d[0][0]))
	if n >= 0:
		f = 'N'
if f == 'N':
	print("False")
else:
	print("True")
