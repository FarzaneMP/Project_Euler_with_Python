### Problem 36 from Project Euler
#https://projecteuler.net/archives

"""The decimal number, 585 = 10010010012 (binary),
 is palindromic in both bases.

Find the sum of all numbers, less than one million,
 which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base,
 may not include leading zeros.)"""

def palindromic (n):
    """input: int
    output: True, False"""
    num_str = str(n)
    if num_str == num_str[::-1]:
        return True
    else:
        return False


def DecimalToBinary(n):
    """Convert decimal to Binary and remove 0b"""
    return bin(n)[2:]

sum = 0
#list = []
for i in range(1,1000000):
    if palindromic(i):
        if palindromic(DecimalToBinary(i)):
            sum += i
            #list.append((i,DecimalToBinary(i) ))
print(sum)
