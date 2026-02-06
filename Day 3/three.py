#Read two numbers and perform all arithmetic operations
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

#output
Enter first number: 10
Enter second number: 5
Addition: 15.0
Subtraction: 5.0
Multiplication: 50.0
Division: 2.0

#---------------------------------------

#Sum and average of three numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

total = a + b + c
average = total / 3

print("Sum:", total)
print("Average:", average)

#output
Enter first number: 10
Enter second number: 20
Enter third number: 30
Sum: 60.0
Average: 20.0

#---------------------------------------
#Area and perimeter of a rectangle
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

area = length * breadth
perimeter = 2 * (length + breadth)

print("Area of rectangle:", area)
print("Perimeter of rectangle:", perimeter)

#output
Enter length: 5
Enter breadth: 3
Area of rectangle: 15.0
Perimeter of rectangle: 16.0

#--------------------------------------------
#Simple Interest calculation

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time (years): "))

si = (p * r * t) / 100
print("Simple Interest:", si)
#output
Enter principal amount: 1000
Enter rate of interest: 2
Enter time (years): 2
Simple Interest: 40.0

#--------------------------------------------
#Square and cube of a number
num = float(input("Enter a number: "))

print("Square:", num * num)
print("Cube:", num * num * num)
#output
Enter a number: 4
Square: 16.0
Cube: 64.0

#------------------------------------------
#Remainder and quotient
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Quotient:", a // b)
print("Remainder:", a % b)
#output
Enter first number: 17
Enter second number: 4
Quotient: 4
Remainder: 1

#----------------------------------------------
#Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit:", fahrenheit)
#output
Enter temperature in Celsius: 35
Temperature in Fahrenheit: 95.0

#------------------------------------------------
#Student total, average, and percentage

print("Average:", average)
print("Percentage:", percentage)m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))
m4 = float(input("Enter marks of subject 4: "))
m5 = float(input("Enter marks of subject 5: "))

total = m1 + m2 + m3 + m4 + m5
average = total / 5
percentage = (total / 500) * 100

print("Total Marks:", total)
#output
Enter marks of subject 1: 70
Enter marks of subject 2: 80
Enter marks of subject 3: 90
Enter marks of subject 4: 100
Enter marks of subject 5: 30
Total Marks: 370.0
Average: 74.0
Percentage: 74.0

#-----------------------------------------------
#Area of a circle
radius = float(input("Enter radius: "))
pi = 3.14

area = pi * radius * radius
print("Area of circle:", area)

#output
Enter radius: 7
Area of circle: 153.86

#----------------------------------------------------
#Profit or loss
cp = float(input("Enter cost price: "))
sp = float(input("Enter selling price: "))

if sp > cp:
    print("Profit:", sp - cp)
elif cp > sp:
    print("Loss:", cp - sp)
else:
    print("No profit no loss")
# output
Enter cost price: 500
Enter selling price: 400
Loss: 100.0

#----------------------------------
