import decimal

funk = input()
D = int(input())
code = compile(funk, "<funk>", "eval")
def f(x):
	return eval(code, {"__builtins__": {}, "abs": abs}, {"x": x})
decimal.getcontext().prec = D + 50
a = decimal.Decimal("-1.5")
b = decimal.Decimal("1.5")
fa = f(a)
N = int(3.33 * (D + 2)) + 20
if fa > 0:
	for i in range(N):
		m = (a + b) / 2
		if f(m) > 0:
			a = m
		else:
			b = m
else:
	for i in range(N):
		m = (a + b) / 2
		if f(m) < 0:
			a = m
		else:
			b = m
root = (a + b) / 2
if abs(root) < decimal.Decimal(10) ** (-(D + 1)):
	root = abs(root)
print(f"{root:.{D}f}")
