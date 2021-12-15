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
		if u.isupper() or vis[u] == 0:
			vis[u] += 1
			dfs(u, f)
			vis[u] -= 1

vis['start'] = 5
dfs('start', 0)

print(ans)