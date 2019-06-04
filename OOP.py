# Object Oriented Python

class Cat:
    pass

cat = Cat()
cat2 = Cat()
# print(cat == cat2) # False


class Dog:

    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

fritz = Dog('Fritz', 3)
print(fritz.name)