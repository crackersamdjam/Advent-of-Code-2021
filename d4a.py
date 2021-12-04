import sys
data = sys.stdin.read().strip().split('\n\n')
nums = list(map(int, data[0].split(',')))

boards = data[1:]
for k in range(len(boards)):
	boards[k] = boards[k].split('\n')
	for i in range(5):
		boards[k][i] = list(map(int, filter(None, boards[k][i].split(' '))))

def done(a):
	for i in range(5):
		if all(not a[i][j] for j in range(5)):
			return 1
		if all(not a[j][i] for j in range(5)):
			return 1
	return 0

for v in nums:
	for k in range(len(boards)):
		for i in range(5):
			for j in range(5):
				if boards[k][i][j] == v:
					boards[k][i][j] = None
		if done(boards[k]):
			print(v*sum(sum(filter(None, row)) for row in boards[k]))
			exit()
