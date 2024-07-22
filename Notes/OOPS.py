# Import necessary modules
from abc import ABC, abstractmethod


# Class
# A blueprint for creating objects.
# Defines a set of attributes and methods that the created objects will have.
class ClassName:
    # class attributes and methods
    pass


# Object:
# An instance of a class.
# Created from a class and represents a specific implementation of the class.
obj = ClassName()


# Attributes:
# Variables that belong to a class or an object.
# Class Attributes: Shared across all instances of a class.
# Instance Attributes: Unique to each instance.
class Dog:
    species = "Canis lupus familiaris"  # class attribute

    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age    # instance attribute


# Methods:
# Functions defined within a class that operate on objects of that class.
class Dogs:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is barking!")


# Encapsulation:
# The bundling of data (attributes) and methods that operate on the data into a single unit (class).
# Provides controlled access to the data.
# Private Attributes and Methods: Prefix with _ or __ to indicate they should not be accessed directly.
class Doggy:
    def __init__(self, name, age):
        self.__name = name  # private attribute
        self.__age = age    # private attribute

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


# Inheritance:
# Allows a class to inherit attributes and methods from another class.
# Promotes code reuse.
# Syntax - class ChildClass(ParentClass):
        # additional attributes and methods

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")


class Doggie(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


# Polymorphism:
# Allows methods to be used interchangeably between different classes.
# Different classes can implement the same method in different ways.
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


animals = [Dog("Buddy", 14), Cat("Whiskers")]

for animal in animals:
    print(animal.speak())

# Abstraction:
# Hiding complex implementation details and showing only the necessary features.
# Achieved using abstract classes and methods in Python.


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"

# These are the basic concepts and usage examples of oops in Python.
# If you have any specific questions or need more detailed explanations, feel free to ask!
# on my LinkedIn- https://www.linkedin.com/in/sarthak-bansal-6744a2256/
# It will help both of us to grow and learn more stuff in python

# Thank You for reading my notes. It means a lot!
