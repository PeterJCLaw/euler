
LENGTHS = {
	0: 0,
	1: 3,
	2: 3,
	3: 5,
	4: 4,
	5: 4,
	6: 3,
	7: 5,
	8: 5,
	9: 4,
	10: 3,
	11: 6,
	12: 7,
	13: 8,
	14: 8,
	15: 7,
	16: 7,
	17: 9,
	18: 8,
	19: 8,
	20: 7,
	30: 6,
	40: 5,
	50: 5,
	60: 5,
	70: 7,
	80: 6,
	90: 6,
	100: 7 + 3,	# hundred and
	1000: 8
}

def length(i):
	length = 0

	thou = i / 1000
	if thou > 0:
		length += LENGTHS[thou] + LENGTHS[1000]
		i -= thou * 1000

	hun = i / 100
	if hun > 0:
		length += LENGTHS[hun] + LENGTHS[100]
		i -= hun * 100

	ten = i / 10
	if ten > 1:
		length += LENGTHS[ten * 10]
		i -= ten * 10

	length += LENGTHS[i]

	return length

print '4:', length(4)	# 4
print '42:', length(42)	# 8
print '342:', length(342)	# 23
print '115:', length(115)	# 20

total = 0

for i in xrange(1, 1001):
	total += length(i)

print total
