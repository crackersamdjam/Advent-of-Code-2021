import sys
data = sys.stdin.read().strip().split('\n\n')

pts = list(map(lambda x: list(map(int, x.split(','))), data[0].split()))

for s in data[1].split('\n'):
	c = int(s[11] == 'y')
	n = int(s[13:])
	for i, p in enumerate(pts):
		if p[c] > n:
			p[c] += 2*(n-p[c])
	break

print(len(set(map(tuple, pts))))