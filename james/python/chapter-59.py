#   Thursday 25/8/22
#   Methods

class Patient():
    def __init__(self, last_name, first_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

james28 = Patient("Anderson", "James", 61)
# Here is a function that checks the age of a patient and displays a message if they are under 21.
def say_if_minor(patient_first_name, patient_last_name, patient_age):
    if patient_age < 21:
        print(patient_first_name + " " + patient_last_name + " is a minor")

# This is the code that calls the function, passing the three attributes of patient james28 as arguments.
say_if_minor(james28.first_name, james28.last_name, james28.age)

# We can build the function into the class itself, which is called a method
# This is how simple it is to call it. Next chapter we will build a method.
james28.say_if_minor()

# You can pass arguments to a method the same way.
james28.say_if_minor("Argument", insured=True)
# insured is a keyword argument
# Argument is a positional arguments