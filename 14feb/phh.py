# Question 1: Perform addition of two numbers using a class
class Add:
    def calc(self, a, b):
        return a + b

obj = Add()
print(obj.calc(5, 3))
# Output
8
#--------------

# Question 2: Find square and cube of a number using a class
class SquareCube:
    def calc(self, n):
        print(n*n)
        print(n*n*n)

obj = SquareCube()
obj.calc(4)
# Output
16
64
#--------------

# Question 3: Calculate simple interest using a class
class SimpleInterest:
    def calc(self, p, t, r):
        return (p*t*r)/100

obj = SimpleInterest()
print(obj.calc(1000, 2, 5))
# Output
100.0
#--------------

# Question 4: Calculate gross salary using a class
class GrossSalary:
    def calc(self, basic):
        hra = basic * 0.2
        da = basic * 0.1
        return basic + hra + da

obj = GrossSalary()
print(obj.calc(10000))
# Output
13000.0
#--------------

# Question 5: Calculate electricity bill using a class
class ElectricityBill:
    def calc(self, units):
        return units * 5

obj = ElectricityBill()
print(obj.calc(100))
# Output
500
#--------------

# Question 6: Calculate total and average marks using a class
class Marks:
    def calc(self, m1, m2, m3):
        total = m1 + m2 + m3
        avg = total / 3
        print(total)
        print(avg)

obj = Marks()
obj.calc(70, 80, 90)
# Output
240
80.0
#--------------

# Question 7: Calculate grade of a student using a class
class Grade:
    def calc(self, avg):
        if avg >= 75:
            print("Distinction")
        elif avg >= 60:
            print("First Class")
        else:
            print("Pass")

obj = Grade()
obj.calc(80)
# Output
Distinction
#--------------

# Question 8: Check whether a student is pass or fail using a class
class Result:
    def calc(self, marks):
        if marks >= 35:
            print("Pass")
        else:
            print("Fail")

obj = Result()
obj.calc(40)
# Output
Pass
#--------------

# Question 9: Store and display multiple student details using a class
class Student:
    def display(self, name, age):
        print(name, age)

obj = Student()
obj.display("Harsha", 20)
obj.display("Ravi", 21)
# Output
Harsha 20
Ravi 21
#--------------

# Question 10: Find highest marks among students using a class
class Highest:
    def calc(self, marks):
        print(max(marks))

obj = Highest()
obj.calc([70, 85, 60])
# Output
85
#--------------

# Question 11: Check whether a number is even or odd using a class
class EvenOdd:
    def calc(self, n):
        if n % 2 == 0:
            print("Even")
        else:
            print("Odd")

obj = EvenOdd()
obj.calc(10)
# Output
Even
#--------------

# Question 12: Check whether a number is prime using a class
class Prime:
    def calc(self, n):
        for i in range(2, n):
            if n % i == 0:
                print("Not Prime")
                return
        print("Prime")

obj = Prime()
obj.calc(7)
# Output
Prime
#--------------

# Question 13: Check whether a number is palindrome using a class
class Palindrome:
    def calc(self, n):
        rev = int(str(n)[::-1])
        if n == rev:
            print("Palindrome")
        else:
            print("Not Palindrome")

obj = Palindrome()
obj.calc(121)
# Output
Palindrome
#--------------

# Question 14: Check whether a year is a leap year using a class
class LeapYear:
    def calc(self, year):
        if year % 4 == 0:
            print("Leap Year")
        else:
            print("Not Leap Year")

obj = LeapYear()
obj.calc(2024)
# Output
Leap Year
#--------------

# Question 15: Perform calculator operations using a class
class Calculator:
    def calc(self, a, b):
        print(a + b)
        print(a - b)
        print(a * b)
        print(a / b)

obj = Calculator()
obj.calc(10, 5)
# Output
15
5
50
2.0
#--------------
