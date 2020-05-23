### Problem 33 from Project Euler
#https://projecteuler.net/archives

"""
The fraction 49/98 is a curious fraction, as an inexperienced
mathematician in attempting to simplify it may incorrectly believe
 that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction,
 less than one in value, and containing two digits in the numerator and
 denominator.
If the product of these four fractions is given in its lowest common terms,
 find the value of the denominator.
"""

import math
List = []

numer = 1
denom = 1

for a in range(1,10):
    for b in range(1,10):
        if a < b:
            for c in range(1,10):
                if (10*a+c)/(10*b+c)==a/b :
                    List.append([10*a+c, 10*b+c])
                    numer *= a
                    denom *= b
                elif (10*c+a)/(10*b+c)==a/b:
                    List.append([10*c+a,10*b+c])
                    numer *= a
                    denom *= b
                elif (10*c+a)/(10*c+b)==a/b:
                    List.append([10*c+a,10*c+b])
                    numer *= a
                    denom *= b
                elif (10*a+c)/(10*c+b)==a/b:
                    List.append([10*a+c, 10*c+b])
                    numer *= a
                    denom *= b

print("Digit cancelling fractions: ", List)
print("numerator:",numer, ", denominator:",denom, ",\
 Highest Common Factor:",math.gcd(numer, denom))
print("Final answer: ", denom/math.gcd(numer, denom))
