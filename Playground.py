import numpy as np

class Animal(object):
    def __init__(self, species, age):
        self.species = species
        self.age = age

    def isPerson(self):
        return self.species == "Homo Sapiens"

    def ageOneYear(self):
        self.age += 1

class Dog(Animal):
    def ageOneYear(self):
        self.age += 7

a = Dog('bird',10)
a.ageOneYear()
# print(a.age)

x = np.array([[6,7],[8,9]])

print (np.size(x))