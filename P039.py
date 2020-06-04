### Problem 39 from Project Euler
#https://projecteuler.net/archives
"""If p is the perimeter of a right angle triangle with integral length sides,
 {a,b,c}, there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}
For which value of p ≤ 1000, is the number of solutions maximised?"""

my_dict = {}
for a in range(1,600):
    for b in range(1,a):
        c = int((a**2+b**2)**0.5)
        if a**2+b**2==int(c)**2:
            P = a + b + c
            if P <= 1000:
                if P in my_dict:
                    my_dict[P].append((a,b,c))
                else:
                    my_dict[P] = [(a,b,c)]

key_max = max(my_dict.keys(), key=(lambda k: len(my_dict[k])))
#key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

print('Maximum Value: ',len(my_dict[key_max]),my_dict[key_max],key_max)
