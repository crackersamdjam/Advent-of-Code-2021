import sys
data = sys.stdin.read().strip().split('\n')

x = y = 0
for s in data:
	s = s.split()
	n = int(s[1])
	if s[0][0] == 'f':
		x += n
	elif s[0][0] == 'd':
		y += n
	else:
		y -= n

print(x*y)