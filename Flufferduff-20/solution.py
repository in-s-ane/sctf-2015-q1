import math
from math import sqrt

'''We define a function *: Z -> {0, 1} in the following way:
*(x) = 1 if {(the sum of all primes in the range (0, n) - the sum of all odd numbers in the range (0, n)) < 0} and 0 otherwise'''

def primeCheck(n):
	if n < 2:
		return False
	else:
		for i in range(2, int(sqrt(n))):
			if (n % i == 0):
				return False
		return True

def oddCheck(n):
	return not (n % 2 == 0)

def flufferduff(n):
	oddSum = 0
	primeSum = 0
	for i in range(1, n):
		if primeCheck(i):
			primeSum += i
		if oddCheck(i):
			oddSum += i
	if (primeSum - oddSum) < 0:
		return 1
	else:
		return 0

def main():
	answer = 0
	for i in range(1, 1000):
		answer += flufferduff(i)
	return answer

print main()
