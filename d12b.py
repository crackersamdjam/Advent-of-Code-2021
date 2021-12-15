import sys
from collections import defaultdict
data = sys.stdin.read().strip().split('\n')

adj = defaultdict(list)
vis = defaultdict(int)
ans = 0

for s in data:
	a, b = s.split('-')
	adj[a].append(b)
	adj[b].append(a)

def dfs(cur, f):
	if cur == 'end':
		global ans
		ans += 1
		return

	for u in adj[cur]:
		vis[u] += 1
		if u.islower() and vis[u] >= 2:
			if f == 0 and u != 'start':
				dfs(u, 1)
		else:
			dfs(u, f)
		vis[u] -= 1

vis['start'] = 5
dfs('start', 0)

print(ans)