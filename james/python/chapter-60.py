# Thursday 25/8/22
#   Coding a method

# When you call a method within a class, you dont need to pass any arguments, as it already has those values.


# Here is the patient class with the method added
class Patient():
    def __init__(self, last_name, first_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
    def say_if_minor(self):
        if self.age > 21:
            print("This patient is a minor")

# The first line of a method definition always takes the same single parameter; self.
# This is the method with concatenated attributes to make up the displayed sentence.
class Patient():
    def __init__(self, last_name, first_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
    def say_if_minor(self):
        if self.age > 21:
            print(self.first_name + " " + self.last_name + " is a minor")