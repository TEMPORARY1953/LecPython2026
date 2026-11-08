import collections

lines = []
while True:
	try:
		line = input()
	except EOFError:
		break
	if line == "":
		break
	lines.append(line)
words = " ".join(lines)
words = words.split()
if not words:
	print("---")
else:
	count = collections.Counter(words)
	maxc = max(count.values())
	res = []
	for w, c in count.items():
		if c == maxc:
			res.append(w)
	if len(res) > 1:
		print("---")
	else:
		print(res[0])
