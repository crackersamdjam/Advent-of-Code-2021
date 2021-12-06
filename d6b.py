import sys
data = sys.stdin.read().strip().split('\n')

a = map(int, data[0].split(','))
arr = [0 for i in range(9)]
for x in a:
	arr[x] += 1

for i in range(256):
	# print(i, sum(arr), arr)
	x = arr.pop(0)
	arr.append(x)
	arr[6] += x

print(sum(arr))
