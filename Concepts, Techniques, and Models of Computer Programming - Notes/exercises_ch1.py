'''
This is a series of notes and exercises done for the book 
'Concepts, Techniques, and Models of Computer Programming' 
By Peter Van Roy

I gave up on learning Mozart while going through this book, 
hoping that I still effectively learn the programming concepts
with different languages. So the following notes and programs 
will be done in Python.
'''
#Getting a better sense of completion time
import timeit
start = timeit.timeit()

# Exercise 1.1a - Calculator 2^100

v = 2*2*2*2*2
w = v*v*v*v*v
x = w*w*w*w

# Exercise 1.1b - Calculator 100!

# with function
def bang(i):
    if i == 1:
        return i
    else:
        return i*bang(i-1)

# print(bang(100))


# # Exercise 1.2 - Better/Smarting factorial calculations

def fact(N):
    if N == 0: 
        return 1
    else:
        return N * fact(N-1)


def fact_limit(N, K):
    if N==K:
        return 1 
    else: 
        return N * fact_limit(N-1, K)

def comb(N, K):
    return fact(N) / (fact(K) * fact(N - K))

def fast_comb(N, K):
    return fact_limit(N, N-K) / fact(K)

# start = timeit.timeit()
# print (comb(500, 200))
# end = timeit.timeit()
# print(end - start)

# start = timeit.timeit()
# print (comb(500, 200))
# end = timeit.timeit()
# print(end - start)

# # Exercise 1.5 - Lazy Order Programming
# # Mozart handles this much more elegently than python, so this is a bit of an experiment
# # getting to perform similarly.

from itertools import islice

#infinite lazy list
def gen_ints(N=0):
    while True:
        yield N
        N += 1 

def sum_list(it_list):
    return sum(it_list)

# creates infinite loop 
# print(sum_list(gen_ints()))

# Exercise 1.6 - Higher order programming
def pascal(n):
    if n <= 1:
        return [1]
    else:
        row = pascal(n-1)
        return op(shift_left(row), shift_right(row))

def op(row_1, row_2):
    return [row_1[x] + row_2[x] for x in range(0,len(row_1))]

def shift_left(row):
    return [0] + row

def shift_right(row):
    return row + [0]

#print(pascal(25))

def generic_pascal(operation, n):
    if n == 1:
        return [1]
    else:
        row = generic_pascal(operation, n-1)
        print(row)
        return op_list(operation, shift_left(row), shift_right(row))

def op_list(operation, row_left, row_right):
    return map(operation, row_left, row_right)

adding = lambda a, b: a + b 
multiply = lambda a, b: (a+1) * (b+1)
doubling = lambda a, b: (a + b) * 2
modible = lambda a, b: (a + b) % (b + 1)

print(generic_pascal(modible, 10))
