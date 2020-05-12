### Problem 15 from Project Euler
#https://projecteuler.net/archives

#Starting in the top left corner of a 2×2 grid,
#and only being able to move to the right and down,
#there are exactly 6 routes to the bottom right corner.
def lattice(x,y):
    """x and y are ints"""
    d = {}
    for i in range(x+1):
        d[(0, i)] = 1
    for j in range(y+1):
        d[(j, 0)] = 1
    for i in range(1,x+1):
        for j in range(1,y+1):
            d[(i, j)] = d[(i-1, j)] +d[(i, j-1)]
    return d[(i,j)]
print(lattice(20,20))
