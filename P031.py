### Problem 31 from Project Euler
#https://projecteuler.net/archives

"""In the United Kingdom the currency is made up of pound
(£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?"""

coins = [1, 2, 5, 10, 20, 50, 100, 200]
def count(S, m, n):
    """input:
     S is a list, m is len(S), n is an int
     Output:
     is the number of ways that n can be achieved
    """
    if n == 0:
        return 1

    if n <= 0:
        return 0

    if m <= 0 and n >= 1:
        return 0

    return count(S, m-1, n)+count(S, m, n-S[m-1])

print(count(coins, len(coins), 200))
