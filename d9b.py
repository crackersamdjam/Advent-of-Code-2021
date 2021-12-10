import sys
a = list(map(lambda x: [int(y) for y in x], sys.stdin.read().strip().split('\n')))

n = len(a)
m = len(a[0])
best = []

for i in range(n):
	for j in range(m):
		if a[i][j] != 9:
			sz = 0
			q = []
			q.append((i, j))
			a[i][j] = 9

			while q:
				ii, jj = q.pop(0)
				sz += 1
				for x in range(max(0, ii-1), 1+min(n-1, ii+1)):
					for y in range(max(0, jj-1), 1+min(m-1, jj+1)):
						if abs(x-ii)+abs(y-jj) == 1 and a[x][y] != 9:
							q.append((x, y))
							a[x][y] = 9

			best.append(sz)

best.sort(reverse=1)
print(best[0]*best[1]*best[2])