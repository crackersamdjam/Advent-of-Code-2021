import sys
data = sys.stdin.read().strip().split('\n')

x = y = a = 0
for s in data:
	s = s.split()
	n = int(s[1])
	if s[0][0] == 'f':
		x += n
		y += a*n
	elif s[0][0] == 'd':
		a += n
	else:
		a -= n

print(x*y)