# 2520 is the smallest number that can be divided by each of the numbers from 1 
# to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the 
# numbers from 1 to 20?


# This problem is small enough that we can "cheat" and just use pen-and-paper 
# maths to identify the prime factors needed to satisfy divisibility by all the
#  numbers from 1 to 20.
print (
         # 1 doesn't matter; any integer will be divisible by 1.
    2 *  # 2 is prime, and must therefore be included.
    3 *  # 3 is prime.
    2 *  # 4 is 2^2, so we need to add another 2 to go with the one we've got.
    5 *  # 5 is prime.
         # 6 is 2*3, and we have both of those already, so we can omit it.
    7 *  # 7 is prime.
    2 *  # 8 is 2^3, so we need another 2.
    3 *  # 9 is 3^2, so we need anoter 3.
         # 10 is 2*5, both of which we have already.
    11 * # 11 is prime.
         # 12 is 2*2*3, and we have all those.
    13 * # 13 is prime.
         # 14 is 2*7.
         # 15 is 3*5.
    2 *  # 16 is 2*4, so we need yet another 2.
    17 * # 17 is prime.
         # 18 is 2*3*3.
    19   # 19 is prime.
         # 20 is 2*2*5.
)