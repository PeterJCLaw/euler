
def fac2(x):
	t=1
	for y in xrange(2,x+1):
		t = t*y
		while t % 10 == 0:
			t = t/10
	return t

total = 0

for c in str(fac2(100)):
	total += int(c)

print total
