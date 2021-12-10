import sys
a = sys.stdin.read().strip().split('\n')

n = len(a)
m = len(a[0])
ans = 0

for i in range(n):
	for j in range(m):
		ok = 1
		for x in range(max(0, i-1), 1+min(n-1, i+1)):
			for y in range(max(0, j-1), 1+min(m-1, j+1)):
				if abs(x-i)+abs(y-j) == 1 and a[x][y] <= a[i][j]:
					ok = 0
		if ok:
			ans += int(a[i][j])+1

print(ans)