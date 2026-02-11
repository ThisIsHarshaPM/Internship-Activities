# Question 16: Count vowels in a string
def count_vowels(s):
    count = 0
    for ch in s:
        if ch in "aeiouAEIOU":
            count += 1
    return count
print(count_vowels("hello"))
# Output
2
#--------------

# Question 17: Check whether a string is palindrome
def string_pal(s):
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")
string_pal("madam")
# Output
Palindrome
#--------------

# Question 18: Find length of a string without built-in function
def length(s):
    count = 0
    for _ in s:
        count += 1
    return count
print(length("Python"))
# Output
6
#--------------

# Question 19: Calculate power of a number
def power(a, b):
    return a ** b
print(power(2, 3))
# Output
8
#--------------

# Question 20: Check whether a number is Armstrong
def armstrong(n):
    temp = n
    s = 0
    while n > 0:
        d = n % 10
        s += d ** 3
        n //= 10
    if s == temp:
        print("Armstrong")
    else:
        print("Not Armstrong")
armstrong(153)
# Output
Armstrong
#--------------

# Question 21: Generate Fibonacci series
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a+b
fibonacci(5)
# Output
0 1 1 2 3
#--------------

# Question 22: Calculate average of numbers in a list
def average(lst):
    return sum(lst)/len(lst)
print(average([10, 20, 30]))
# Output
20.0
#--------------

# Question 23: Check positive, negative or zero
def check(n):
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")
check(-5)
# Output
Negative
#--------------

# Question 24: Find the smallest number in a list
def smallest(lst):
    return min(lst)
print(smallest([4, 1, 7]))
# Output
1
#--------------

# Question 25: Count even and odd numbers in a list
def count_even_odd(lst):
    even = odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    print("Even:", even)
    print("Odd:", odd)
count_even_odd([1,2,3,4])
# Output
Even: 2
Odd: 2
#--------------

# Question 26: Calculate gross salary
def gross(basic):
    hra = basic * 0.2
    da = basic * 0.1
    return basic + hra + da
print(gross(10000))
# Output
13000.0
#--------------

# Question 27: Find GCD of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
print(gcd(12, 18))
# Output
6
#--------------

# Question 28: Find LCM of two numbers
def lcm(a, b):
    return (a*b)//gcd(a, b)
print(lcm(4, 6))
# Output
12
#--------------

# Question 29: Calculate electricity bill
def bill(units):
    return units * 5
print(bill(100))
# Output
500
#--------------

# Question 30: Display prime numbers within a range
def primes(a, b):
    for n in range(a, b+1):
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            if n > 1:
                print(n, end=" ")
primes(1, 10)
# Output
2 3 5 7
#--------------
