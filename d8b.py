import sys
from itertools import permutations
data = sys.stdin.read().strip().split('\n')

def go(a):
	return [''.join(sorted(x)) for x in a]

ans = 0
nums = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
gonums = sorted(go(nums))

for s in data:
	s = s.split('|')
	a = s[0].split()
	b = s[1].split()
	for p in permutations('abcdefg'):
		p = ''.join(p)
		tmp = nums[:]
		ok = 0

		cur = [''.join(list(map(lambda c: chr(ord('a') + p.index(c)), x))) for x in a]
		cur = sorted(go(cur))

		if cur == gonums:
			cur = [''.join(list(map(lambda c: chr(ord('a') + p.index(c)), x))) for x in b]
			cur = go(cur)

			ans += int(''.join(str(nums.index(x)) for x in cur))
			break

print(ans)