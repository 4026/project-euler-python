# A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 × 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindromic(x):
    string = str(x)
    for i in range(0, int(len(string) / 2) + 1):
        if string[i] != string[-(i + 1)]:
            return False
    return True

i = 999
max_found = 0
while (i * 999 > max_found):
    j = 999
    product = i * j
    while(product > max_found):
        if (is_palindromic(product)):
            print("%d * %d = %d" % (i, j, product))
            max_found = product
        j -= 1
        product = i * j
    i -= 1