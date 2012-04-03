sum = 0
done = False
fib = 1
last_fib = 0
last_fib2 = 0
while not done:
	print 'fib = ',fib
	last_fib2 = last_fib
	last_fib = fib
	fib = fib + last_fib2
	if fib > 4000000:
		done = True
		break
	if fib % 2 == 0:
		sum = sum + fib

print 'sum = ',sum
