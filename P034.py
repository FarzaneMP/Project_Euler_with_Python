### Problem 31 from Project Euler
#https://projecteuler.net/archives


"""145 is a curious number,
as 1!+ 4!+5!= 1+ 24+ 120= 145.

Find the sum of all numbers which are equal to the
 sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums
 they are not included."""

def fact(n, d={0:1, 1:1}):
    if n in d:
        return d[n]
    else:
        d[n] = fact(n-1,d)*n
        return d[n]

list = []
for i in range(10,1000000):
    num_str = str(i)
    len_num_str = len(num_str)
    sum_fact_digits = 0
    for digit in range(len_num_str):
        sum_fact_digits += fact(int(num_str[digit]))
    if sum_fact_digits == i:
        list.append(i)


print((sum(list)))
