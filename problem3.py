# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def prime_factors(x):
    factors = []
    i = 2
    while (x > 1):
        if (x % i == 0):
            x /= i
            factors.append(i)
        else:
            i += 1
    return factors

print(max(prime_factors(600851475143)))