import sys
data = sys.stdin.read().strip().split('\n')

ans = 0
for s in data:
	s = s.split('|')
	a = s[0].split()
	b = s[1].split()
	for c in b:
		ans += len(c) in [2, 4, 3, 7]

print(ans)