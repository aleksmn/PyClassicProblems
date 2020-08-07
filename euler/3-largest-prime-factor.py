import logging
import math

logging.basicConfig(level=logging.DEBUG)

# Находим множители (делители) числа

def getFactors(number):
    factors = []
    for potentialFactor in range(1, int(math.sqrt(number)) + 1):
        if number % potentialFactor == 0:
            factors.append(potentialFactor)
            factors.append(number // potentialFactor)
    return(factors)

# Определяем, множитель простое число или нет

def isPrime(number):
    return(len(getFactors(number)) == 2)

# Находим простые множители
# способ 1


##def getPrimeFactors(number):
##    primeFactors=[]
##    for factor in getFactors(number):
##        if isPrime(factor) == True:
##            primeFactors.append(factor)
##    return(primeFactors)
##
##def largestPrimeFactor(number):
##    return getPrimeFactors(number)[-1]
##

# способ 2

def getLargestPrimeFactor(number):
    allFactors = getFactors(number)
    largestPrime = 0
    for factor in allFactors:
        if isPrime(factor) and factor > largestPrime:
            largestPrime = factor
    return largestPrime

logging.debug('getLargestPrimeFactor(600851475143) = %s'
              % getLargestPrimeFactor(600851475143))

# Для числа 600851475143
# Ответ: 6857



    
    
 
