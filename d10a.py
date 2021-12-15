import sys
data = sys.stdin.read().strip().split('\n')

ans = 0
for s in data:
	l = ['z']
	for c in s:
		if c == ')':
			if l[-1] == '(':
				l.pop(-1)
			else:
				ans += 3
				break
		elif c == ']':
			if l[-1] == '[':
				l.pop(-1)
			else:
				ans += 57
				break
		elif c == '}':
			if l[-1] == '{':
				l.pop(-1)
			else:
				ans += 1197
				break
		elif c == '>':
			if l[-1] == '<':
				l.pop(-1)
			else:
				ans += 25137
				break
		else:
			l.append(c)

print(ans)