# generate fib numbers

fibNumbers = [1, 2]

while fibNumbers[-1] < 4000000:
    fibNumbers.append(fibNumbers[-1] + fibNumbers[-2])

del(fibNumbers[-1])

# find all even nums

evenFibNums=[]

for fibNumber in fibNumbers:
    if fibNumber % 2 == 0:
        evenFibNums.append(fibNumber)

# sum all of even nums

sumOfEvens = 0

for num in evenFibNums:
    sumOfEvens += num

print(sumOfEvens)

# Answer: 4613732
