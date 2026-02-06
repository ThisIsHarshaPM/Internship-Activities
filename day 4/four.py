# Question 1: Write a Python program to check whether a given year is a leap year or not

# Answer
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# Output
# Enter a year: 2024
# Leap Year

#--------------

# Question 2: Write a Python program to check whether a given character is a vowel or consonant

# Answer
ch = input("Enter a character: ").lower()

if ch in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:
    print("Consonant")

# Output
# Enter a character: a
# Vowel

#--------------

# Question 3: Write a Python program to calculate grade of a student based on percentage

# Answer
percentage = float(input("Enter percentage: "))

if percentage >= 90:
    print("Grade A")
elif percentage >= 75:
    print("Grade B")
elif percentage >= 60:
    print("Grade C")
elif percentage >= 40:
    print("Grade D")
else:
    print("Fail")

# Output
# Enter percentage: 82
# Grade B

#--------------

# Question 4: Write a Python program to check whether a given number is a palindrome or not

# Answer
num = input("Enter a number: ")

if num == num[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

# Output
# Enter a number: 121
# Palindrome

#--------------

# Question 5: Write a Python program to find whether a given number is divisible by both 5 and 11

# Answer
num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both 5 and 11")

# Output
# Enter a number: 55
# Divisible by both 5 and 11

#--------------

# Question 6: Write a Python program to calculate electricity bill based on units consumed

# Answer
units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = (100 * 1.5) + (units - 100) * 2.5
else:
    bill = (100 * 1.5) + (100 * 2.5) + (units - 200) * 4

print("Electricity Bill =", bill)

# Output
# Enter units consumed: 150
# Electricity Bill = 275.0

#--------------

# Question 7: Write a Python program to check whether a given number is a prime number

# Answer
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")
else:
    print("Not a Prime Number")

# Output
# Enter a number: 7
# Prime Number

#--------------

# Question 8: Write a Python program to check whether a given character is an alphabet, digit, or special character

# Answer
ch = input("Enter a character: ")

if ch.isalpha():
    print("Alphabet")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Character")

# Output
# Enter a character: @
# Special Character

#--------------

# Question 9: Write a Python program to find the roots of a quadratic equation

# Answer
import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

d = b*b - 4*a*c

if d > 0:
    r1 = (-b + math.sqrt(d)) / (2*a)
    r2 = (-b - math.sqrt(d)) / (2*a)
    print("Roots are", r1, "and", r2)
elif d == 0:
    r = -b / (2*a)
    print("Root is", r)
else:
    print("No real roots")

# Output
# Enter a: 1
# Enter b: -5
# Enter c: 6
# Roots are 3.0 and 2.0

#--------------

# Question 10: Write a Python program to calculate bonus of an employee based on salary

# Answer
salary = float(input("Enter salary: "))

if salary >= 50000:
    bonus = salary * 0.10
else:
    bonus = salary * 0.05

print("Bonus =", bonus)

# Output
# Enter salary: 60000
# Bonus = 6000.0

#--------------

# Question 11: Write a Python program to determine the type of triangle

# Answer
a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

# Output
# Enter side 1: 5
# Enter side 2: 5
# Enter side 3: 8
# Isosceles Triangle

#--------------

# Question 12: Write a Python program to calculate attendance eligibility for exam

# Answer
total_classes = int(input("Enter total classes: "))
attended = int(input("Enter attended classes: "))

percentage = (attended / total_classes) * 100

if percentage >= 75:
    print("Eligible for Exam")
else:
    print("Not Eligible for Exam")

# Output
# Enter total classes: 100
# Enter attended classes: 80
# Eligible for Exam
