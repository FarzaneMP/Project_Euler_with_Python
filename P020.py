### Problem 20 from Project Euler
#https://projecteuler.net/archives

#Find the sum of the digits in the number 100!
def fact(n):
    """The function calculates n!
    n is an it"""
    n_fact = 1
    for i in range(1,n+1):
        n_fact *= i
    return n_fact


def sum_of_digits(Num):
    """This function calculates
    sum of the digits of a number
    Num is an int"""
    sum_digits = 0
    for j in range(len(str(Num))):
        sum_digits += int(str(Num)[j])
    return sum_digits

if __name__ == "__main__":
    print(sum_of_digits(fact(100)))
