import sys
data = sys.stdin.read().strip().split('\n')

m = len(data[0])
a = [0]*m

for s in data:
	for i in range(m):
		a[i] += 1 if s[i] == '1' else -1

x = sum((1<<m-1-i)*(a[i] > 0) for i in range(m))
print(x*(((1<<m)-1)^x))
