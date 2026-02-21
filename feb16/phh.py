# Question 1: Create a text file and write data into it
f = open("data.txt", "w")
f.write("Hello Python\nFile Handling Basics")
f.close()
print("File created")
# Output
File created
#--------------

# Question 2: Read the contents of a file
f = open("data.txt", "r")
print(f.read())
f.close()
# Output
Hello Python
File Handling Basics
#--------------

# Question 3: Append data to an existing file
f = open("data.txt", "a")
f.write("\nAppending new line")
f.close()
print("Data appended")
# Output
Data appended
#--------------

# Question 4: Count number of lines in a file
f = open("data.txt", "r")
lines = f.readlines()
print(len(lines))
f.close()
# Output
3
#--------------

# Question 5: Count number of words in a file
f = open("data.txt", "r")
words = f.read().split()
print(len(words))
f.close()
# Output
6
#--------------

# Question 6: Count number of characters in a file
f = open("data.txt", "r")
text = f.read()
print(len(text))
f.close()
# Output
39
#--------------

# Question 7: Copy contents of one file to another file
f1 = open("data.txt", "r")
f2 = open("copy.txt", "w")
f2.write(f1.read())
f1.close()
f2.close()
print("File copied")
# Output
File copied
#--------------

# Question 8: Display file contents line by line
f = open("data.txt", "r")
for line in f:
    print(line.strip())
f.close()
# Output
Hello Python
File Handling Basics
Appending new line
#--------------

# Question 9: Search for a specific word in a file
f = open("data.txt", "r")
text = f.read()
if "Python" in text:
    print("Word Found")
else:
    print("Word Not Found")
f.close()
# Output
Word Found
#--------------

# Question 10: Display only even-numbered lines
f = open("data.txt", "r")
lines = f.readlines()
for i in range(len(lines)):
    if (i + 1) % 2 == 0:
        print(lines[i].strip())
f.close()
# Output
File Handling Basics
#--------------

# Question 11: Find the largest word in a file
f = open("data.txt", "r")
words = f.read().split()
print(max(words, key=len))
f.close()
# Output
Handling
#--------------

# Question 12: Replace a word in a file with another word
f = open("data.txt", "r")
text = f.read()
f.close()

text = text.replace("Python", "JAVA")

f = open("data.txt", "w")
f.write(text)
f.close()
print("Word replaced")
# Output
Word replaced
#--------------

# Question 13: Remove blank lines from a file
f = open("data.txt", "r")
lines = f.readlines()
f.close()

f = open("data.txt", "w")
for line in lines:
    if line.strip():
        f.write(line)
f.close()
print("Blank lines removed")
# Output
Blank lines removed
#--------------

# Question 14: Count frequency of each word in a file
f = open("data.txt", "r")
words = f.read().split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
print(freq)
f.close()
# Output
{'Hello': 1, 'JAVA': 1, 'File': 1, 'Handling': 1, 'Basics': 1, 'Appending': 1, 'new': 1, 'line': 1}
#--------------

# Question 15: Merge two files into a third file
f1 = open("data.txt", "r")
f2 = open("copy.txt", "r")
f3 = open("merge.txt", "w")

f3.write(f1.read())
f3.write("\n")
f3.write(f2.read())

f1.close()
f2.close()
f3.close()
print("Files merged")
# Output
Files merged
#--------------
