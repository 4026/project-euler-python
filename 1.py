# If we list all the natural numbers below 10 that are multiples 
# of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def triangular(n):
    return int((n * (n+1)) / 2)

def sumOfMultiples(multiplier, max):
    return triangular(int(max / multiplier)) * multiplier

print(sumOfMultiples(3, 999) + sumOfMultiples(5, 999) - sumOfMultiples(15, 999))