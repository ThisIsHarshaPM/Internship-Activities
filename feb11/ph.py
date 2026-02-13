# Question 1: Create a list of integers and display it
lst = [1, 2, 3, 4, 5]
print(lst)
# Output
[1, 2, 3, 4, 5]
#--------------

# Question 2: Find sum and average of list elements
lst = [10, 20, 30]
print("Sum:", sum(lst))
print("Average:", sum(lst)/len(lst))
# Output
Sum: 60
Average: 20.0
#--------------

# Question 3: Find largest and smallest element in a list
lst = [4, 7, 1, 9]
print(max(lst))
print(min(lst))
# Output
9
1
#--------------

# Question 4: Count even and odd numbers in a list
lst = [1, 2, 3, 4]
even = odd = 0
for i in lst:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(even, odd)
# Output
2 2
#--------------

# Question 5: Remove duplicate elements from a list
lst = [1, 2, 2, 3]
print(list(set(lst)))
# Output
[1, 2, 3]
#--------------

# Question 6: Reverse a list
lst = [1, 2, 3]
lst.reverse()
print(lst)
# Output
[3, 2, 1]
#--------------

# Question 7: Sort list in ascending order
lst = [5, 2, 4, 1]
lst.sort()
print(lst)
# Output
[1, 2, 4, 5]
#--------------

# Question 8: Search for an element in a list
lst = [10, 20, 30]
print(20 in lst)
# Output
True
#--------------

# Question 9: Merge two lists
a = [1, 2]
b = [3, 4]
print(a + b)
# Output
[1, 2, 3, 4]
#--------------

# Question 10: Find second largest element in a list
lst = [4, 6, 1, 9]
lst.sort()
print(lst[-2])
# Output
6
#--------------

# Question 11: Create a tuple and display elements
t = (1, 2, 3)
print(t)
# Output
(1, 2, 3)
#--------------

# Question 12: Find length of a tuple
t = (10, 20, 30)
print(len(t))
# Output
3
#--------------

# Question 13: Find maximum and minimum in a tuple
t = (5, 1, 9)
print(max(t))
print(min(t))
# Output
9
1
#--------------

# Question 14: Convert tuple into list
t = (1, 2, 3)
print(list(t))
# Output
[1, 2, 3]
#--------------

# Question 15: Check whether element exists in a tuple
t = (10, 20, 30)
print(20 in t)
# Output
True
#--------------
