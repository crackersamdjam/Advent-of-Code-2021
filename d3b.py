import sys
a = sys.stdin.read().strip().split('\n')
b = a[:]
m = len(a[0])

for i in range(m):
	ca = 0
	for s in a:
		ca += 1 if s[i] == '1' else -1
	na = []
	for s in a:
		if (ca >= 0) == (s[i] == '1'):
			na.append(s)
	a = na

	cb = 0
	for s in b:
		cb += 1 if s[i] == '1' else -1
	nb = []
	for s in b:
		if (cb < 0) == (s[i] == '1') or len(b) == 1:
			nb.append(s)
	b = nb

# print(a, b)
# print(int(a[0], 2))
# print(int(b[0], 2))
print(int(a[0], 2)*int(b[0], 2))
