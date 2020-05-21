### Problem 31 from Project Euler
#https://projecteuler.net/archives

"""A unit fraction contains 1 in the numerator.
The decimal representation of the unit fractions
with denominators 2 to 10 are given:

1/2	= 0.5, 1/3= 0.(3), 1/4= 0.25, 1/5= 0.2, 1/6	= 0.1(6)
1/7	= 0.(142857)

Where 0.1(6) means 0.166666...,
and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the
longest recurring cycle in its decimal fraction part.

"""
def reciprocal_len(n):
    count = 0
    x = 1
    list = []
    while count < n and x!=0:
        x = (10*x) %n
        if x in list:
            return len(list)
        list.append(x)
        count += 1
    return 0

max_len = 6
num_with_max_len = 1
for i in range(1000,2, -1):
    if max_len > i:
        break
    if reciprocal_len(i) > max_len:
        max_len = reciprocal_len(i)
        num_with_max_len = i

print('number:', num_with_max_len, ', reciprocal length:', max_len)
