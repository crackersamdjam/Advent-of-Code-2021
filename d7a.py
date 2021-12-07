import sys
data = sys.stdin.read().strip().split('\n')

a = sorted(list(map(int, data[0].split(','))))

m = a[len(a)//2]
print(sum(abs(x-m) for x in a))
