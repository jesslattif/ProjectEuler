"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

# How to find the largest prime factor of n:
# start at 2
# divide the number by successive odd integers i up to sqrt(n)
# when remainder is 0, return max i, find largest prime factor n/i

import math

def lgst_prime_factor(n):
	for i in range(2, int(math.sqrt(n))):
		if i % 2 != 0 and n % i == 0:
			k = n/i
			print i, k
			lgst_prime_factor(k)


lgst_prime_factor(600851475143)
