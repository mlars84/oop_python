# Review 1
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

daisy_mae = Dog('Diasy', 10)
fritz = Dog('Fritz', 3)
turtle_bean = Dog('Turtle', 2)

def get_biggest_number(*args):
    return max(args)

# print("The oldest dog is {} years old".format(
#     get_biggest_number(daisy_mae.age, fritz.age, turtle_bean.age)
# )) # The oldest dog is 10 years old


# Review 2
# Parent class
class Cat:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

# Child class (inherits from Cat class)
class Tabby(Cat):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# Child class (inherits from Cat class)
class MaineCoon(Cat):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

class Pets:
    cats = []

    def __init__(self, cats):
        self.cats = cats
cats = [
    Tabby('Jerry', 6),
    MaineCoon('Hugo', 5),
    Dog('Larry', 2)
]

pets = Pets(cats)

for cat in pets.cats:
    print(cat.name)

    

    