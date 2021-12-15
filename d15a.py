import sys
arr = sys.stdin.read().strip().split('\n')
n = len(arr)
m = len(arr[0])
inq = [[0 for i in range(m)] for i in range(n)]
dis = [[10**9 for i in range(m)] for i in range(n)]

dis[0][0] = 0
q = [(0, 0)]

def ok(x, y):
	return x >= 0 and x < n and y >= 0 and y < m
def mv(x, y):
	for a, b in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
		if ok(a, b):
			yield (a, b)

while q:
	x, y = q.pop(0)
	inq[x][y] = 0
	curd = dis[x][y]
	for a, b in mv(x, y):
		if curd+int(arr[a][b]) < dis[a][b]:
			dis[a][b] = curd+int(arr[a][b])
			if inq[a][b] == 0:
				inq[a][b] = 1
				q.append((a, b))

print(dis[-1][-1])