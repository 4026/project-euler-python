# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see 
# that the 6th prime is 13.
# 
# What is the 10,001st prime number?

sieve = []
n_primes = 0
i = 2
while(n_primes < 10001):
    is_prime = True
    for d in sieve:
        if (i % d == 0):
            is_prime = False
            break
    if is_prime:
        sieve.append(i)
        n_primes += 1
    i += 1

print(sieve[-1])