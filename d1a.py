import sys
a = list(map(int, sys.stdin.read().split()))
ans = 0
for i in range(1, len(a)):
	ans += a[i] > a[i-1]
print(ans)
