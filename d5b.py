import sys
data = sys.stdin.read().strip().split('\n')

a = [[0 for i in range(1000)] for j in range(1000)]

def d(x):
	return x//abs(x) if x else 0

for s in data:
	s = list(map(int, s.replace(' -> ', ',').split(',')))
	dx, dy = d(s[2]-s[0]), d(s[3]-s[1])
	while s[0] != s[2] or s[1] != s[3]:
		a[s[0]][s[1]] += 1
		s[0] += dx
		s[1] += dy
	a[s[2]][s[3]] += 1

print(sum(sum(x > 1 for x in row) for row in a))