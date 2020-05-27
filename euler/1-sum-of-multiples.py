# Find the sum of all the multiples of 3 or 5 below 1000.

# Configure of debugging
import logging
# Set debug level
logging.basicConfig(level=logging.DEBUG)

multiples=[]

for number in range(1000):
	if number % 3 == 0 or number % 5 == 0:
		multiples.append(number)

# logging.debug(multiples)

sumOfMultiples = 0

for multiple in multiples:
    sumOfMultiples += multiple

# print(sumOfMultiples)


## Second method


mult3 = list(range(0, 1000, 3))
mult5 = list(range(0, 1000, 5))

mult3and5 = list(set(mult3+mult5))

print(sum(mult3and5))



