# Problem 1 from Project Euler
#https://projecteuler.net/archives

"""If we list all the natural numbers below 10 that are multiples of 3 or 5,
 we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000."""
def multiples(x, y, z):
    """ x, y, z -> int
    returnt all the multiples of y or z below x """
    sum = 0
    for i in range(x):
        if i%y == 0 or i%z == 0:
            sum += i
    return sum

if __name__ == "__main__":
	print(multiples(1000, 3, 5))
