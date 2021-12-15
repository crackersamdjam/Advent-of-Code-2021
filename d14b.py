import sys
from collections import defaultdict
data = sys.stdin.read().strip().split('\n')
s = data[0]
mp = dict()

cur = defaultdict(int)

for x in data[2:]:
	mp[x[0:2]] = x[6]

for i in range(1, len(s)):
	p = s[i-1]+s[i]
	cur[p] += 1

cur[' '+s[0]] += 1
cur[s[-1]+' '] += 1

for t in range(40):
	nx = defaultdict(int)
	for p, k in cur.items():
		if p in mp:
			c = mp[p]
			nx[p[0]+c] += k
			nx[c+p[1]] += k
		else:
			nx[p] += k
	cur = nx

cnt = defaultdict(int)
for p, k in cur.items():
	cnt[p[0]] += k
	cnt[p[1]] += k
del cnt[' ']
print((max(cnt.values()) - min(cnt.values())) // 2)