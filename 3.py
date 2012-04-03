num = 600851475143
for i in range(int(num**0.5), num, 2):
	print i
	if num % i == 0 and is_prime(i):
		print i
		break

prime_list	= [2, 3, 5, 7, 11, 13, 17, 19, 23]
def is_prime(n):
	#see if it's big enough
	if n < 2:
		return False
	#see if it's a known prime
	if n in prime_list:
		return True

	#see if it's divisible by any known prime
	for i in prime_list:
		if (1.0*n/i) == int(n/i):
			print '',n,' is diivisble by ',i,' which is prime'
			return False;

	#do a brute-force test to find a divisor
	for i in range(max(prime_list), int(n**0.5), 2):
		if (1.0*n/i) == int(n/i):
			print '',n,' is diivisble by ',i
			return False;

	#else it must be a new prime
	prime_list.append(n)

	return True;


#print is_prime(num)

print prime_list
