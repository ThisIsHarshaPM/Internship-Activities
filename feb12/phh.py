# Question 16: Create a set and display elements
s = {1, 2, 3}
print(s)
# Output
{1, 2, 3}
#--------------

# Question 17: Union, intersection and difference of sets
a = {1, 2, 3}
b = {3, 4}
print(a | b)
print(a & b)
print(a - b)
# Output
{1, 2, 3, 4}
{3}
{1, 2}
#--------------

# Question 18: Remove duplicates from list using set
lst = [1, 2, 2, 3]
print(list(set(lst)))
# Output
[1, 2, 3]
#--------------

# Question 19: Find common elements between two sets
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)
# Output
{2, 3}
#--------------

# Question 20: Check whether one set is subset of another
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))
# Output
True
#--------------

# Question 21: Create dictionary of student details
student = {"name": "Harsha", "age": 20}
print(student)
# Output
{'name': 'Harsha', 'age': 20}
#--------------

# Question 22: Add new key-value pair to dictionary
student["marks"] = 90
print(student)
# Output
{'name': 'Harsha', 'age': 20, 'marks': 90}
#--------------

# Question 23: Delete a key from dictionary
del student["age"]
print(student)
# Output
{'name': 'Harsha', 'marks': 90}
#--------------

# Question 24: Search for a key in dictionary
print("name" in student)
# Output
True
#--------------

# Question 25: Find sum of all values in dictionary
d = {"a": 10, "b": 20}
print(sum(d.values()))
# Output
30
#--------------

# Question 26: Count frequency of elements in a list
lst = [1, 2, 2, 3]
freq = {}
for i in lst:
    freq[i] = freq.get(i, 0) + 1
print(freq)
# Output
{1: 1, 2: 2, 3: 1}
#--------------

# Question 27: Merge two dictionaries
d1 = {"a": 1}
d2 = {"b": 2}
d1.update(d2)
print(d1)
# Output
{'a': 1, 'b': 2}
#--------------

# Question 28: Print keys and values separately
d = {"x": 10, "y": 20}
print(d.keys())
print(d.values())
# Output
dict_keys(['x', 'y'])
dict_values([10, 20])
#--------------

# Question 29: Find maximum and minimum value in dictionary
d = {"a": 5, "b": 2, "c": 9}
print(max(d.values()))
print(min(d.values()))
# Output
9
2
#--------------

# Question 30: Sort dictionary by keys
d = {"b": 2, "a": 1}
print(dict(sorted(d.items())))
# Output
{'a': 1, 'b': 2}
#--------------
