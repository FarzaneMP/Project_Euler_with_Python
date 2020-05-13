### Problem 21 from Project Euler
#https://projecteuler.net/archives

#Let d(n) be defined as the sum of proper divisors of n
#(numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a ≠ b,
#then a and b are an amicable pair and each of a and b
#are called amicable numbers.
def sum_divisor(x, d={}):
    """x is an int and this function
    calculates the sum of divisors of x"""
    sum = 0
    for i in range(1, x):
        if x%i == 0:
            sum += i
    d[x] = sum
    return d


def sum_value(d):
    """d is a dict and
    the function calculates sum of
    values in d """
    sum_val = 0
    for value in d.values():
        sum_val += value
    return sum_val

dict_sum_divisor ={}
d_Amicable = {}
for i in range(10000):
    sum_divisor(i, dict_sum_divisor)

for key,value in dict_sum_divisor.items():
    if value in dict_sum_divisor:
        if dict_sum_divisor[value] == key:
            if dict_sum_divisor[value] != value:
                d_Amicable[key] = value

print(sum_value(d_Amicable))
