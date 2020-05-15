### Problem 25 from Project Euler
#https://projecteuler.net/archives

#What is the index of the first
#term in the Fibonacci sequence to contain 1000 digits?

fib = [0, 1]
i = 2
while True:
    fib_n = fib[i-1]+fib[i-2]
    fib.append(fib_n)
    if len(str(fib_n)) >= 1000:
        print(i)
        break
    i += 1
