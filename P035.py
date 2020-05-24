### Problem 29 from Project Euler
#https://projecteuler.net/archives

"""The number, 197, is called a circular prime because all rotations of the digits:
 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?"""
def is_prime(n):
    if n==2:
        return True
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
print(is_prime(2))
circular_prime = []
circular_prime_family = []
for i in range(2,1000000):
    prime = False
    count = 0
    if is_prime(i):
        num_str = str(i)
        len_num = len(num_str)
        sub_list = []
        for j in range(len_num):
            if is_prime(int(num_str[j:]+num_str[:j])):
                prime = True
                sub_list.append(int(num_str[j:]+num_str[:j]))
            else:
                prime = False
                break
        if prime:
            sub_list.sort()
            circular_prime.append(i)
            if sub_list not in circular_prime_family:
                circular_prime_family.append(sub_list)

print(circular_prime_family)
print("Total circular prime numbers less than 1 million: ",len(circular_prime))
