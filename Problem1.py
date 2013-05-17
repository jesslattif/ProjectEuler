"""find sum of all multiples of 3 or 5 below 1000:

first: find all multiples of 3 or 5 in range 1-1000

second: add them"""

total = 0
for num in range(1, 1000):
	if num % 3 == 0 or num %5 == 0:
		total = total + num 
print total

		

