# This file defines a class called 'person'
# and gives it objects name, age, and height

class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

# Test Script for Person Class
# new_person = Person(name='Joe', age=34, height=184)
# print("{:} is {:} years old and is {:}cm tall.".format(new_person.name, new_person.age, new_person.height))