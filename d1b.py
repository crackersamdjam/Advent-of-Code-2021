import sys
a = list(map(int, sys.stdin.read().split()))
ans = 0
def val(i):
	return a[i]+a[i-1]+a[i-2]
for i in range(1, len(a)):
	ans += val(i) > val(i-1)
print(ans)
