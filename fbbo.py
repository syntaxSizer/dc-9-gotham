#/usr/bin/python
n = 55
def fib(n): #write Fibonacci up to n
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a+b

fib(n)
