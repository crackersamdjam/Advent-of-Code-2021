import sys
data = sys.stdin.read().strip().split('\n\n')

pts = list(map(lambda x: list(map(int, x.split(','))), data[0].split()))

for s in data[1].split('\n'):
	c = int(s[11] == 'y')
	n = int(s[13:])
	for i, p in enumerate(pts):
		if p[c] > n:
			p[c] += 2*(n-p[c])
			assert p[c] >= 0

n = max(x[1] for x in pts)+1
m = max(x[0] for x in pts)+1
g = [['.' for j in range(m)] for i in range(n)]
for x, y in pts:
	g[y][x] = '#'

print('\n'.join(''.join(r) for r in g))
# EFJKZLBL