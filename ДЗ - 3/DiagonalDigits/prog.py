s = input()
M, N = map(int, s.split(','))
cnt = [0] * (M + N - 1)
q = 0

for i in range(M + N - 1):
	if i < N and i < M:
		q += 1
		cnt[i] = q
	elif i >= N and i >= M:
		q -= 1
		cnt[i] = q
	else:
		cnt[i] = q
		
s = [0] * (M + N - 1)
acc = 0
for d in range(M + N - 1):
	s[d] = acc
	acc += cnt[d]
	
for i in range(N):
	for j in range(M):
		d = i + j
		if d % 2 == 1:
			print((s[d] + min(N - 1, d) - i) % 10, end=' ')
		else:
			print((s[d] + i - max(0, d - (M - 1))) % 10, end=' ')
	print()
