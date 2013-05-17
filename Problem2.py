"""Find the sum of all even fibonacci numbers below 4 million"""

#fibonacci:

import math

mylist = []

def fibo():
# """This is the long & slow way"""
# # if n == 0:
# #     return 0
# # elif n == 1:
# # 	return 1
# # else:
# #     return fibo(n - 1) + fibo(n - 2)
# """ this is the faster way """
	current = 0
	last = 1
	while current <= 4000000:
		temp = current
		current = current + last
		last = temp
		mylist.append(current)
		current += 0

sumlist = []
def sum_even_fibos():
	for i in mylist:
		if i % 2 == 0:
			sumlist.append(i)
	print sum(sumlist)



