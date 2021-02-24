#!/usr/bin/env python
from IPython.display import display
import numpy as np
import matplotlib.pyplot as plt

from person import Person

list_of_names = ['Roger', 'Mary', 'Luisa', 'Elvis']
list_of_ages = [23, 24, 19, 86]

list_of_names = ['Roger', 'Mary', 'Luisa', 'Elvis']
list_of_ages  = [23, 24, 19, 86]
list_of_heights_cm = [175, 162, 178, 182]

for name in list_of_names:
  print("The name {:} is {:} letters long".format(name, len(name)))

new_list = [len(x) for x in list_of_names]    # Part B: List Comprehensions
display(new_list)                             # Displays a list of lengths of the given names


people = {}                     # Part E: Dictionary of People Objects, Key is person's name
for i in range(len(list_of_names)):
  people[list_of_names[i]] = Person(
    name=list_of_names[i],
    age=list_of_ages[i],
    height=list_of_heights_cm[i]
  )
display(people)                 # Display's Person Class Return Strings in Dictionary

# Part F: Numpy Arrays of Each List containing Integers
array_age = np.array(list_of_ages)
array_height = np.array(list_of_heights_cm)

# Part G: Average Age
average_age = np.mean(array_age)
print(f"The average age of the people is {average_age}")

# Part H: Scatter Plot of Ages to Heights of People
plt.plot(array_age[:], array_height[:], '.')
plt.xlabel("Age")
plt.ylabel("Height")
plt.title("Plot of People's Ages to Heights")
plt.grid(True)
plt.show()
