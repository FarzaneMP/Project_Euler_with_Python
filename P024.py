### Problem 24 from Project Euler
#https://projecteuler.net/archives

#What is the millionth lexicographic permutation of
#the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

from itertools import permutations

def lexicographic_permutation(l, n):
    """Create lexicographic permutation(sorted list)
    l is a list of numbers and n=len(l)"""
    permutation = list(permutations(l, n))
    permutation_num = sorted([int(''.join(tups)) for tups in permutation])
    return permutation_num

l = ['0','1', '2','3','4','5','6','7','8','9']
#print(permutations(l, 3))
list = lexicographic_permutation(l, len(l))
print(list[1000000-1])
