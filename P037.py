### Problem 37 from Project Euler
#https://projecteuler.net/archives
"""The number 3797 has an interesting property. Being prime itself,
it is possible to continuously remove digits from left to right, and remain prime at each stage:
 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes."""


def is_prime(n):
    if n==2:
        return True
    if n==1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True


number = 11
count = 1
truncatable_primes = []
while count < 12:
    truncatable = False
    if is_prime(number):
        str_num = str(number)
        for j in range(len(str_num)):
            if is_prime(int(str_num[j:])):
                truncatable = True
            else:
                truncatable = False
                break
        if truncatable:
            for j in range(len(str_num)):
                if is_prime(int(str_num[:j+1])):
                    truncatable = True
                else:
                    truncatable = False
                    break
        if truncatable:
            truncatable_primes.append(number)
            count += 1
    number += 1

print(sum(truncatable_primes))
