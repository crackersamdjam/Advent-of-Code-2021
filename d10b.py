import sys
data = sys.stdin.read().strip().split('\n')

val = {'(': 1, '[': 2, '{': 3, '<': 4}
ans = []

for s in data:
	l = ['z']
	ok = 1
	for c in s:
		if c == ')':
			if l[-1] == '(':
				l.pop(-1)
			else:
				ok = 0
				break
		elif c == ']':
			if l[-1] == '[':
				l.pop(-1)
			else:
				ok = 0
				break
		elif c == '}':
			if l[-1] == '{':
				l.pop(-1)
			else:
				ok = 0
				break
		elif c == '>':
			if l[-1] == '<':
				l.pop(-1)
			else:
				ok = 0
				break
		else:
			l.append(c)
	if ok:
		l.pop(0)
		cur = 0
		for c in l[::-1]:
			cur = cur*5 + val[c]
		ans.append(cur)

ans.sort()
print(ans[len(ans)//2])