### Problem 28 from Project Euler
#https://projecteuler.net/archives
"""Starting with the number 1 and moving to the right in a clockwise
 direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001
spiral formed in the same way?"""

list = [[1]]
add = 1
start = 1
n = 1001
l = []
for i in range (1,int(n/2)+1):
    l = []
    start += i*2
    for j in range (1,4):
        l.append(start)
        add += start
        start += i*2
    l.append(start)

    list.append(l)
    
#sum of nested lists
sum_diagonals = sum([element for sub_list in list for element in sub_list])
print(sum_diagonals)
