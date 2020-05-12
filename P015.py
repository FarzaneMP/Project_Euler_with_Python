### Problem 15 from Project Euler
#https://projecteuler.net/archives

#Starting in the top left corner of a 2×2 grid,
#and only being able to move to the right and down,
#there are exactly 6 routes to the bottom right corner.
def lattice(x, y, d):
    """ x and y are integers and
    d is the dictionary {(0,1): 1, (1,0): 1}
    I used Memoization """
    if (x,y) in d :
        return d[(x, y)]
    elif x==0 or y==0:
        return 1
    else:
        ans1 = lattice(x-1, y, d)
        ans2 = lattice(x, y-1, d)
        d[(x-1, y)] = ans1
        d[(x, y-1)] = ans2

        return ans1+ans2

d = {(0,1): 1, (1,0): 1}
print(lattice(20,20, d))
