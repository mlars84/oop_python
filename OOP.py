# Object Oriented Python

class Cat:
    pass

cat = Cat()
cat2 = Cat()
# print(cat == cat2) # False


class CurrentDog:

    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    # The __init__ method gets called any time you create a new instance.
    def __init__(self, name, age = 1):
        self.name = name
        self.age = age
    
    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

fritz = CurrentDog('Fritz', 2.5)
# print(fritz.age)
turtle_bean = CurrentDog('Turtle Bean', float(1.34))
# print(fritz.name) # Fritz
# print(fritz.species) # mammal
# print(fritz.description())
# print(fritz.speak('Aruuff!'))

if turtle_bean.species == "mammal":
    print("{0} is a {1}!".format(turtle_bean.name, turtle_bean.species))



class Email:
    def __init__(self, address):
        self.address = address
        self.is_sent = False
    def send_email(self):
        self.is_sent = True
    def change_address(self, new_address):
        self.address = new_address

my_email = Email('matt.a.larson@gmail.com')
# print('Before: ', my_email.is_sent)
my_email.send_email()
# print('After: ', my_email.is_sent)
# print(my_email.address)
my_email.change_address('test@example.com')
# print(my_email.address)



# Python Object Inheritance
# Parent class
class Dog:

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

class AmericanBulldog(Dog):
    def sleep_amount(self, amount_in_hours):
        return "{} sleeps {} hours a day at least.".format(self.name, amount_in_hours)

# Child class (inherits from Dog class)
class GermanShepard(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

daisy = AmericanBulldog('Daisy Mae', 10)
# print(daisy.name) # Daisy Mae
print(daisy.sleep_amount(13))