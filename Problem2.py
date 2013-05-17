"""Find the sum of all even fibonacci numbers below 4 million"""

# total = 0
# for num in range(1, 1000):
# 	if num % 3 == 0 or num %5 == 0:
# 		total = total + num 
# print total


#fibonacci:

def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# mylist = []
for i in xrange(1, 20):
	mylist = [fibonacci(i) if fibonacci(i % 2) == 0]:
#     	mylist.append(i)
#     else:
#     	pass

	print mylist
	# print fibonacci(i)