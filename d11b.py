import sys
a = [list(map(int, list(x))) for x in sys.stdin.read().strip().split('\n')]
ans = 0

def mv(x, y):
	for i in range(x-1, x+2):
		for j in range(y-1, y+2):
			if i >= 0 and i <= 9 and j >= 0 and j <= 9:
				yield (i, j)

t = 0
while 1:
	t += 1
	for i in range(10):
		for j in range(10):
			a[i][j] += 1
	vis = set()
	again = 1
	while again:
		again = 0
		for i in range(10):
			for j in range(10):
				if a[i][j] > 9 and (i, j) not in vis:
					vis.add((i, j))
					again = 1
					for x, y in mv(i, j):
						a[x][y] += 1
	for x, y in vis:
		a[x][y] = 0

	if len(vis) == 100:
		print(t)
		break
