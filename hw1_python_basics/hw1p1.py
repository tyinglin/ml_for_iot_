#!/usr/bin/env python
from IPython.display import display
import person

list_of_names = ['Roger', 'Mary', 'Luisa', 'Elvis']
list_of_ages  = [23, 24, 19, 86]
list_of_heights_cm = [175, 162, 178, 182]

for name in list_of_names:
  print("The name {:} is {:} letters long".format(name, len(name)))

new_list = [len(x) for x in list_of_names]    # Part 1: List Comprehensions
display(new_list)                             # Displays a list of lengths of the given names


  

