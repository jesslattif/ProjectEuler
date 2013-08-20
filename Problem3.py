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

# def lgst_prime_factor(primes_list, number):
# 	factors_list = []
# 	for num in primes_list:
# 		if number % num == 0:
# 			factors_list.append(num)
# 	return factors_list


# def main():
# 	input_prime_file = open("primes2.txt") #create variable from text file in args
# 	primes_string = input_prime_file.read() # creates variable primes from text file
# 	input_prime_file.close() #closes text file
# 	primes_and_junk = [space.strip() for space in primes_string.split(' ')]#strips spaces & newlines out of file
# 	primes_list = [int(num) for num in primes_and_junk if num != ""] #can this go faster??
# 	# check_data(primes_list)
# 	lgst_prime_factor(primes_list, 600851475143)


# if __name__ == "__main__":
# 	main()