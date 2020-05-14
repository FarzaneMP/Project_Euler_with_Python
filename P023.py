### Problem 20 from Project Euler
#https://projecteuler.net/archives

#ind the sum of all the positive integers which cannot be
#written as the sum of two abundant numbers.
def abundant(x, d=[]):
    """x is an int and this function
    calculates the sum of divisors of x and
    returns a list of abundant numbers x< sum_divisor"""
    sum = 0
    for i in range(1, x):
        if x%i == 0:
            sum += i
    if sum > x:
        l.append(x)
    return l

l = []
for i in range(1,28123):# finding the list of abundants for less than 28123
                        #all integers greater than 28123 can be written as
                        #the sum of two abundant numbers
    abundant(i, l)

list_all = [x for x in range(1, 28123)]#list of numbers from 1 to 28123
l2 = []

for i in l:#list of sum of all abundant numbers less than 28123
    for j in l:
        if i+j<28123:
            l2.append(i+j)

nonabundant = list(set(l2)^set(list_all))#keeping just the unique values in list_all

if __name__=='__main__':
    print(sum(nonabundant ))
