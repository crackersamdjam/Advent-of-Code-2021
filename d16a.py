import sys
ins = sys.stdin.read().strip()
ins = '{:032b}'.format(int(ins, 16)).zfill(len(ins)*4)
ptr = 0
ans = 0

def get(k):
	global ptr
	ret = ins[ptr:ptr+k]
	ptr += k
	return ret

def go():
	global ans
	st = ptr
	ver = int(get(3), 2)
	ans += ver
	id = int(get(3), 2)
	if id == 4:
		tot = ''
		while 1:
			s = get(5)
			tot += s[1:]
			if s[0] == '0':
				break
	else:
		lentype = get(1)
		if lentype == '0':
			totlen = int(get(15), 2)
			while totlen > 0:
				totlen -= go()
			assert totlen == 0
		elif lentype == '1':
			numpack = int(get(11), 2)
			for _ in range(numpack):
				go()
		else:
			assert 0
	dis = ptr-st
	return dis

go()
print(ans)

# 3 bits - package version in binary
# 3 bits - package id in binary

# id = 4 -> literal value packet
# 	groups of 5 bits
#   first of each 5 tells you if it's the last group (if it's a 0)
#   data is 4 other bits
# entire data is all data concatenated

# operator packet:
# 	7th bit is length type ID
#   if 0, next 15 bits mean total length in bits of subpackets
#   if 1, next 11 bits mean # of subpackets
# then, the subpackets appear

# add up all of the version numbers
