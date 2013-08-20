"""
CanadaUSA Mathcamp Python Crash Course Workshop
This is the file produced during the workshop on 7/18/13
Presented by Lewis Ellis and Lucas Garron
"""
print 'hello'
 
a = 3
print a
a = 5
print a
b = 3.6
 
c = 'string'
print b
print c
 
d = True
print d
 
print (a == 5)
 
print type(a), type(b), type(c), type(d)
 
print 3 + 2
# + - * /
print 3+2, 5-3, 6*2, 8/4
# % **
print 7 % 3, 2**5
 
print 2**10000
 
print 'Math'*3+'camp'
print 'Bunni'*2+'toki'*2
 
print a + b
 
l = [1,2,3,4,5]
print l
l = [1,2,'hello', True]
print l
print l[0], l[2]
print l[-1]
 
print len(c), len(l)
print round(3.4), round(3.6)
print int(3.6), int(3.4), str(5), float(3)
 
print bool(''), bool(0), bool([])
print bool('anything'), bool(2), bool([1,2,3])
 
def f(x):
  return x*2
 
print f(3), f(7), f('math'), f([1,2,3])
 
def g(x,y):
  return x+y
 
print g(1,2), g([1,2],[3,4])
 
if (a == 6):
  print 'true is true!'
else:
  print 'false is not true!'
 
if (a == 4):
  print 4
elif (a == 6):
  print 6
else:
  print 5
 
b1 = True
b2 = True
b3 = False
if (b1 and b2) or not b3:
  print 'that is a true expression'
 
l = range(3,6)
print l
l = range(5)
print l
 
# for .. in
total = 0
for item in l:
  total = total + item
  total += item
  print item
print total
 
def factorial(x):
  if x == 0:
    return 1
  else:
    total = 1
    for n in range(1,x+1):
      total = total * n
    return total
print factorial(3), factorial(6)
print len(str(factorial(10000)))
 
def list_sum(l):
  total = 0
  for item in l:
    total = total + item
  return total
print list_sum(range(1000000))
print sum(range(1000000))
 
# Calculate the product of each number in a list with its index
l = [3, 7, 8, 11]
print l[2]
total = 0
for i in range(len(l)):
  total = total + l[i] * i
print total
 
# Calculate the sum of every number 1 through 1000 which is
# a multiple of 3 or a multiple of 5
total = 0
for x in range(1000):
  if (x % 3 == 0) or (x % 5 == 0):
    total = total + x
print total
 
def is_prime(x):
  if x < 2:
    return False
  for divisor in range(2, int(x**0.5)+1):
    if x % divisor == 0:
      return False
  return True
 
for i in range(2,9):
  print i, 'is prime?', is_prime(i)
 
a = 64
while a > 4:
  print a
  a = a / 2
print a
 
a = 5
while True:
  a = a + 1
  if a > 8:
    break
print a
 
# What is the 10,001st prime number?
currently_checking = 0
number_of_primes_found = 0
while number_of_primes_found < 10001:
  currently_checking = currently_checking + 1
  if is_prime(currently_checking):
    number_of_primes_found = number_of_primes_found + 1
print currently_checking
 
if True:
  a = 10
print a
def f(x):
  a = 11
  return x
print f(3)
print a
 
import math
print math.sqrt(9)
print math.pi, math.e
print math.ceil(3.2)
 
import random
for i in range(3):
  print random.random()
 
l = []
for i in range(4):
  l.append(i*2)
print l
 
"""
  Recursive factorial definition:
  0! = 1
  n! = n*(n-1)!
"""
def factorial_recursive(x):
  if x == 0:
    return 1
  else:
    return x*factorial_recursive(x-1)
 
print factorial_recursive(6)
 
# fib(1) = fib(2) = 1
# fib(n) = fib(n-1) + fib(n-2)
def fib(n):
  if n < 3:
    return 1
  else:
    return fib(n-1) + fib(n-2)
 
for i in range(10):
  print fib(i)
 
fibs = [1,1,2,3,5,8,13,21,34]
def fib_smarter(n):
  if n-1 < len(fibs):
    return fibs[n-1]
  else:
    fibs.append(fib_smarter(n-1) + fib_smarter(n-2))
  return fibs[n-1]
 
print fib_smarter(4)
print fib_smarter(5)
print fib_smarter(7)
for i in range(30, 50):
  print fib_smarter(i)
 
n = 1
while math.log(fib_smarter(n), 10)+1 < 1000:
  n = n + 1
print fib_smarter(n)
print n
 
l = []
for i in range(10):
  if i % 2 == 0:
    l.append(2**i)
print l
 
print [2**i for i in range(10) if i%2 == 0]
 
matrix = [[1,0,0],
      [0,1,0],
      [0,2,1]]
print matrix
print matrix[0]
print matrix[0][0]
print matrix[2][1]
 
for char in 'hello':
  print char
 
"""
Things to look at/google for:
Learn python the hard way
codecademy
learnpython.org
documentation on python.org
 
Problems to try:
projecteuler.net
6, 8, 14, 15, 29, 30
 
Email Lewis:
  sillelewis@gmail.com
Email Lucas:
  See www.garron.us
 
"""