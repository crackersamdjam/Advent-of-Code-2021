import sys
import numpy as np
ins = sys.stdin.read().strip()
ins = '{:032b}'.format(int(ins, 16)).zfill(len(ins)*4)
ptr = 0

def get(k):
	global ptr
	ret = ins[ptr:ptr+k]
	ptr += k
	return ret

def go():
	st = ptr
	ver = int(get(3), 2)
	id = int(get(3), 2)
	if id == 4:
		val = ''
		while 1:
			s = get(5)
			val += s[1:]
			if s[0] == '0':
				break
		val = int(val, 2)
	else:
		l = []
		lentype = get(1)
		if lentype == '0':
			totlen = int(get(15), 2)
			while totlen > 0:
				subval, sublen = go()
				l.append(subval)
				totlen -= sublen
			assert totlen == 0
		elif lentype == '1':
			numpack = int(get(11), 2)
			for _ in range(numpack):
				l.append(go()[0])
		else:
			assert 0
		if id == 0:
			val = sum(l)
		elif id == 1:
			val = np.prod(l)
		elif id == 2:
			val = min(l)
		elif id == 3:
			val = max(l)
		elif id == 5:
			assert len(l) == 2
			val = l[0] > l[1]
		elif id == 6:
			assert len(l) == 2
			val = l[0] < l[1]
		elif id == 7:
			assert len(l) == 2
			val = l[0] == l[1]
		else:
			assert 0

	dis = ptr-st
	return val, dis

print(go()[0])

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

# ID
# 0 sum
# 1 prod
# 2 min
# 3 max
# 5 > (subpack[0] > subpack[1] (exactly 2 subpacks))
# 6 <
# 7 =
