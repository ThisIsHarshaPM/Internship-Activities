# Question 1: Find the sum of two numbers
def add(a, b):
    return a + b
print(add(5, 3))
# Output
8
#--------------

# Question 2: Check whether a number is even or odd
def even_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
even_odd(10)
# Output
Even
#--------------

# Question 3: Find the factorial of a number
def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f
print(factorial(5))
# Output
120
#--------------

# Question 4: Check whether a number is prime
def prime(n):
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            return
    print("Prime")
prime(7)
# Output
Prime
#--------------

# Question 5: Find the maximum of two numbers
def max_two(a, b):
    return a if a > b else b
print(max_two(4, 9))
# Output
9
#--------------

# Question 6: Find the maximum of three numbers
def max_three(a, b, c):
    return max(a, b, c)
print(max_three(3, 8, 5))
# Output
8
#--------------

# Question 7: Calculate simple interest
def simple_interest(p, t, r):
    return (p * t * r) / 100
print(simple_interest(1000, 2, 5))
# Output
100.0
#--------------

# Question 8: Calculate the area of a circle
def area_circle(r):
    return 3.14 * r * r
print(area_circle(7))
# Output
153.86
#--------------

# Question 9: Find square and cube of a number
def square_cube(n):
    print("Square:", n*n)
    print("Cube:", n*n*n)
square_cube(4)
# Output
Square: 16
Cube: 64
#--------------

# Question 10: Check whether a year is a leap year
def leap(year):
    if year % 4 == 0:
        print("Leap Year")
    else:
        print("Not Leap Year")
leap(2024)
# Output
Leap Year
#--------------

# Question 11: Reverse a number
def reverse(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev
print(reverse(123))
# Output
321
#--------------

# Question 12: Check whether a number is palindrome
def palindrome(n):
    if n == reverse(n):
        print("Palindrome")
    else:
        print("Not Palindrome")
palindrome(121)
# Output
Palindrome
#--------------

# Question 13: Find the sum of digits of a number
def sum_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s
print(sum_digits(123))
# Output
6
#--------------

# Question 14: Convert Celsius to Fahrenheit
def c_to_f(c):
    return (c * 9/5) + 32
print(c_to_f(30))
# Output
86.0
#--------------

# Question 15: Find the largest element in a list
def largest(lst):
    return max(lst)
print(largest([4, 7, 2, 9]))
# Output
9
#--------------
