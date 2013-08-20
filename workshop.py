"""
This is the template/reference file I originally prepared for a fast-paced
Python Crash Course which I gave to students at Canada/USA Mathcamp 2013.
This was built with a mathy audience in mind, and with a goal of giving
them some basic python-bashing skills to help with Puzzle Hunt problems
I hope to build this into a more general workshop for a broader audience.

To note: a lot of the code in this file can be nitpicked in one way or another.
But I made some pretty intentional decisions based on the context of the workshop.
So I probably have considered the alternatives, and intentionally excluded them
for the sake of not overloading students with too many rules or ways of doing things
With this considered, I welcome feedback or suggestions.
"""
# Python intro workshop
# This is a comment - we can use them to explain what's going on!

print 'Hello world'
print 'Hello', 'world'

# We can assign values to variables
# Use a single = sign to do this
a = 5
print a
# And we can change them after we assign them
a = 7
print a
# We only use = for assigning values; for comparing, use ==
print a == 5
print a == 7

# a is an integer, but we can store different types of things
# Floating point numbers (type float)
b = 3.14
print b
print type(b)

# Strings (type str) - some text surrounded by quotes
c = 'Mathcamp'
print c
print type(c)

# 'Boolean' types - True or False
d = True
print d
print type(d)
print type(a==6)

# We can do stuff with values
# Basic math operators: + - * /
print 10*3, 4+5, 7-5, 6/3
# They follow order of operations, and parentheses work like you think
print (10*3+5)/7-2
# We also have some other operators:
print 2**5, 31 % 7
# Note: python can bash through massive numbers pretty well!
print 2**10000
# We can compare values with ==
print 3 == 2, True == False, a == 5
# These operators behave differently with different types
print 'Math' + 'camp'
print 'Bunni' * 2 + 'Toki' * 2

print 'a is:', a

a = 3
b = 5
print (a + b)

# We have functions that do things for us:
print len('Mathcamp'), round(2.1), round(2.6)
# And functions for casting between types:
print str(10), int(2.1), int(2.6), float(2)
# And casting to bool:
print bool(None), bool(''), bool(0), bool('hello'), bool(2)

# We can define our own functions:
def f(x):
    return (x+1)**2

# Functions can take more than one argument:
def g(x,y):
    return (x+y)**2

print f(2), g(2,3)

# We can make decisions based on booleans:
if True:
    print 'true is true!'

# Python knows how the logic flow works by how we indent it
# Use the tab key to do this

if a == 6:
    print 'a == 6'
elif a == 4:
    print 'a == 4'
else:
    print 'a is something else'

# We can build expressions with and, or, and not

b1 = True
b2 = True
b3 = False
if (b1 and b2) or not b3:
    print 'The expression is true!'
else:
    print 'The expression is false!'

# We can have lists of things:
l = [1,2,3,4,5]
print l, len(l)

# We can index into lists
# The first item is index 0; we can also use negative indices to start at the end
print l[0], l[1], l[4], l[-1]

# You can iterate over lists and do something with each element
# range(m,n) gives us the list [m,m+1,..,n-2,n-1], range(n) = range(0,n)
# Let's iterate over each index of a list:
total = 0
for i in range(len(l)):
    total = total + l[i]
print total

# But we don't need to iterate over the indices and index into the list every time
# We can just iterate over the list's values themselves:
total = 0
for element in l:
    print element
    total = total + element
print total

# Let's use a loop to write factorial(n):
def factorial(n):
    if n == 0:
        return 1
    else:
        product = 1
        for i in range(1, n+1):
            product = product * i
        return product

# And we can write a general sum function:
def list_sum(l):
    total = 0
    for i in l:
        total = total + i
    return total

l = [1,2,3,4,5,10]
print list_sum(l)
# But what do you know, python already gives us one:
print sum(l)

# We can even have lists of lists - like matrices
I3 = [[1, 0, 0],
      [0, 1, 0],
      [0, 0, 1]]

print I3[0][0], I3[1][1], I3[2][2]
# Which 0 is this referring to?
print I3[2][1]

# Let's use what we have to solve Project Euler #1
# Find the sum of all the multiples of 3 or 5 below 1000
total = 0
for i in range(1001):
    if i % 3 == 0 or i % 5 == 0:
        total = total + i
print total

# Of course, we could have done that mathematically, but that's not always so easy
# Let's write a function to determine if a number is prime.
def is_prime(n):
    for i in range(2, n/2+1):
        if n % i == 0:
            return False
    return True

for i in range(2,10):
    print 'is', i, 'prime?', is_prime(i)

# Sometimes we want to do stuff beyond the basics.
# Lots of libraries exist in Python to help us do stuff.
# To use them, we import them, then access their stuff as libraryname.item
import math
print math.sqrt(9)
print math.pi, math.e

import random
for i in range(5):
    print random.random()

# Now we have math.sqrt, so we can do isPrime more intelligently:
def is_prime_smart(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

# We've seen for loops. Let's introduce another kind of loop: while loops
a = 64
while a > 2:
    print a
    a = a / 2
print a

# Let's use these last two pieces to solve Project Euler #7:
# What is the 10 001st prime number?
primes = []
last_prime = 1
while len(primes) < 10001:
    current = last_prime + 1
    while not is_prime_smart(current):
        current = current + 1
    primes.append(current)
    last_prime = current
print primes[10000]

# We can do stuff recursively - functions can call themselves.
# Let's use this to redefine factorial, following the more classic definition:
def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)

# Now let's use that to solve PE # 25:
# What is the first term in the Fibonacci sequence to contain 1000 digits?
def fib(n):
    if n < 3:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print fib(5)
print fib(20)
print fib(30)
print fib(31)

# This is really slow! We're never going to get to 1000 digits at this rate.
# What's going on? Why so slow? How can we do it faster?
# You have to be careful with recursion - sometimes it's not the best way!
fibs = [1,1,2,3,5,8]
def fib_better(n):
    while n > len(fibs):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[n-1]

n = 1
while True:
    n = n + 1
    fn = fib_better(n)
    if len(str(fn)) >= 1000:
        print fn
        break

# Now what? Go forth and work on some stuff. We will be here to help.
# PE 6
# PE 8
# PE 9
# PE 14
# PE 15
# PE 29
# PE 30
# Maybe an example puzzle hunt problem?


# Resources for learning more
# codecademy
# learn python the hard way
# learnpython.org
# Finding/reading docs


# Advanced topics - everything from here is a maybe

# List comprehensions
# We have some nice shorthand for building lists
# [exp for item in list if condition]
l = []
for i in range(20):
    if is_prime_smart(i):
        l.append(i)
print l
# This does the same thing:
print [i for i in range(20) if is_prime_smart(i)]

# File i/o
# read a file, do something, write a file

# Functional stuff
# map, reduce, filter, lambda

# Web stuff
# point curious individuals at flask

print 'finished'