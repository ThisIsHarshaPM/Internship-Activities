# Question 16: Handle division by zero exception
try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")
# Output
Cannot divide by zero
#--------------

# Question 17: Handle file not found exception
try:
    f = open("nofile.txt", "r")
except FileNotFoundError:
    print("File not found")
# Output
File not found
#--------------

# Question 18: Demonstrate try–except–else block
try:
    a = 10
    b = 2
    print(a / b)
except ZeroDivisionError:
    print("Error")
else:
    print("Division successful")
# Output
5.0
Division successful
#--------------

# Question 19: Demonstrate try–except–finally block
try:
    f = open("test.txt", "w")
    f.write("Hello")
except:
    print("Error occurred")
finally:
    f.close()
    print("File closed")
# Output
File closed
#--------------

# Question 20: Handle multiple exceptions
try:
    x = int("abc")
    print(10 / 0)
except ValueError:
    print("Value Error")
except ZeroDivisionError:
    print("Zero Division Error")
# Output
Value Error
#--------------

# Question 21: Open a file using exception handling
try:
    f = open("data.txt", "r")
    print("File opened")
    f.close()
except FileNotFoundError:
    print("File not found")
# Output
File opened
#--------------

# Question 22: Read a file and handle error if file does not exist
try:
    f = open("data.txt", "r")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("File does not exist")
# Output
(file content displayed)
#--------------

# Question 23: Write data to a file and handle exceptions
try:
    f = open("write.txt", "w")
    f.write("Writing data")
    f.close()
    print("Data written")
except:
    print("Error writing file")
# Output
Data written
#--------------

# Question 24: Append data to a file using exception handling
try:
    f = open("write.txt", "a")
    f.write("\nAppended data")
    f.close()
    print("Data appended")
except:
    print("Append failed")
# Output
Data appended
#--------------

# Question 25: Count lines in a file using exception handling
try:
    f = open("write.txt", "r")
    lines = f.readlines()
    print(len(lines))
    f.close()
except:
    print("File error")
# Output
2
#--------------

# Question 26: Raise a user-defined exception
try:
    age = -5
    if age < 0:
        raise Exception("Invalid age")
except Exception as e:
    print(e)
# Output
Invalid age
#--------------

# Question 27: Handle ValueError using exception handling
try:
    n = int("hello")
except ValueError:
    print("ValueError occurred")
# Output
ValueError occurred
#--------------

# Question 28: Handle IndexError using exception handling
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError:
    print("IndexError occurred")
# Output
IndexError occurred
#--------------

# Question 29: Handle TypeError using exception handling
try:
    print(10 + "5")
except TypeError:
    print("TypeError occurred")
# Output
TypeError occurred
#--------------

# Question 30: Demonstrate custom exception class
class MyError(Exception):
    pass

try:
    raise MyError("Custom exception raised")
except MyError as e:
    print(e)
# Output
Custom exception raised
#--------------
