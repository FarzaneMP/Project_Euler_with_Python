### Problem 27 from Project Euler
#https://projecteuler.net/archives
"""
n^2+an+b, where |a|<1000 and |b|≤1000
Find the product of the coefficients, a and b,
 for the quadratic expression that produces
 the maximum number of primes for consecutive values of n,
 starting with n=0."""

def is_prime(x):
    """input: integer
    Output: True if it is prime"""
    if x <= 0:
        return False
    if x == 2:
        return True
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            return False

    return True

prime_count_max = 0
for a in range(-999,1000):
    for b in range(-1000, 1001):
        n = 0
        while is_prime(n*n + a*n + b):
            x = n**2 + a*n + b
            n += 1

        if prime_count_max < n:
            #print(prime_count)
            prime_count_max = n
            a_max = a
            b_max = b

print ("a*b= ",(a_max* b_max))
