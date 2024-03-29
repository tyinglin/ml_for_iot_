# This file defines a class called 'person'
# and gives it objects name, age, and height
# Part C: Person Class

class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __repr__(self):     # Part D: Return String of Object Formatted
        return "{:} is {:} years old and {:}cm tall.".format(self.name, self.age, self.height)

# Test Script for Person Class
# new_person = Person(name='Joe', age=34, height=184)
# print("{:} is {:} years old and is {:}cm tall.".format(new_person.name, new_person.age, new_person.height))