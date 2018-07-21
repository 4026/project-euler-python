def triangular(n):
    return int((n * (n+1)) / 2)

def sumOfMultiples(multiplier, max):
    return triangular(int(max / multiplier)) * multiplier

print(sumOfMultiples(3, 999) + sumOfMultiples(5, 999) - sumOfMultiples(15, 999))