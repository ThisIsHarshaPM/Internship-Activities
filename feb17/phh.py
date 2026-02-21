# Question 1: Plot a simple line graph (1 to 10 and their squares)
import matplotlib.pyplot as plt

x = list(range(1, 11))
y = [i*i for i in x]

plt.plot(x, y)
plt.show()
# Output
Graph displayed
#--------------

# Question 2: Plot two lines y=x and y=x^2
import matplotlib.pyplot as plt

x = list(range(1, 11))
plt.plot(x, x)
plt.plot(x, [i*i for i in x])
plt.show()
# Output
Graph displayed
#--------------

# Question 3: Create a graph and add grid
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,6,8,10]

plt.plot(x, y)
plt.grid()
plt.show()
# Output
Graph displayed
#--------------

# Question 4: Create a bar chart showing marks of 5 students
import matplotlib.pyplot as plt

students = ["A","B","C","D","E"]
marks = [70, 80, 65, 90, 75]

plt.bar(students, marks)
plt.show()
# Output
Graph displayed
#--------------

# Question 5: Create a horizontal bar chart
import matplotlib.pyplot as plt

students = ["A","B","C","D","E"]
marks = [70, 80, 65, 90, 75]

plt.barh(students, marks)
plt.show()
# Output
Graph displayed
#--------------

# Question 6: Draw a pie chart of 5 subjects
import matplotlib.pyplot as plt

subjects = ["Math","Phy","Chem","Bio","CS"]
marks = [80,70,75,85,90]

plt.pie(marks, labels=subjects, autopct='%1.1f%%')
plt.show()
# Output
Graph displayed
#--------------

# Question 7: Create a scatter plot (height vs weight)
import matplotlib.pyplot as plt

height = [150,160,170,180]
weight = [50,60,70,80]

plt.scatter(height, weight)
plt.show()
# Output
Graph displayed
#--------------

# Question 8: Plot a sine wave
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

plt.plot(x, y)
plt.show()
# Output
Graph displayed
#--------------

# Question 9: Plot multiple subplots in one figure
import matplotlib.pyplot as plt

plt.subplot(1,2,1)
plt.plot([1,2,3],[4,5,6])

plt.subplot(1,2,2)
plt.bar([1,2,3],[3,2,1])

plt.show()
# Output
Graph displayed
#--------------

# Question 10: First subplot – Line graph
import matplotlib.pyplot as plt

plt.subplot(2,1,1)
plt.plot([1,2,3],[2,4,6])
plt.show()
# Output
Graph displayed
#--------------

# Question 11: Second subplot – Bar graph
import matplotlib.pyplot as plt

plt.subplot(2,1,2)
plt.bar([1,2,3],[3,6,9])
plt.show()
# Output
Graph displayed
#--------------

# Question 12: Create a histogram using random data
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(100)
plt.hist(data)
plt.show()
# Output
Graph displayed
#--------------

# Question 13: Plot real-time sensor data simulation
import matplotlib.pyplot as plt
import random

temp = [random.randint(20,30) for _ in range(10)]
plt.plot(temp)
plt.show()
# Output
Graph displayed
#--------------

# Question 14: Create a graph with legend, colors, font size, background
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,25,30]

plt.plot(x, y, label="Line", color="red")
plt.legend(fontsize=10)
plt.gca().set_facecolor("lightyellow")
plt.show()
# Output
Graph displayed
#--------------
