### Problem 16 from Project Euler
#https://projecteuler.net/archives

#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2^1000?
def power(x,n):
    """This function calculate x^n
    n is an integer"""
    ans = 1
    for i in range(n):
        ans *=x
    return ans


def sum_of_digits(Num):
    """This function calculate
    sum of the digits of a number
    Num is an int"""
    sum_digits = 0
    for j in range(len(str(Num))):
        sum_digits += int(str(Num)[j])
    return sum_digits

if __name__ == "__main__":
    print(sum_of_digits(power(2,1000)))
