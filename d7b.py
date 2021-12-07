import sys
data = sys.stdin.read().strip().split('\n')

a = sorted(list(map(int, data[0].split(','))))

def dist(x):
	return x*(x+1)//2

def val(m):
	return sum(dist(abs(x-m)) for x in a)

l = a[0]
r = a[-1]
while l <= r:
	m = l+r>>1
	if val(m) < val(m+1):
		r = m-1
	else:
		l = m+1

print(val(l))
