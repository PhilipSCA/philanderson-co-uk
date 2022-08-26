date = "Friday 26/08/22"
print(date)

# Accessing the class

class Patient():
  def __init__(self, last_name, first_name, age):
    self.last_name = last_name
    self.first_name = first_name
    self.age = age

pid4343 = Patient("Taleb", "Sue", 61)
pid4344 = Patient("Anand", "Punya", 29)
pid4345 = Patient("Lin", "Lilly", 48)
pid1298 = Patient("Nilsson", "Rhonda", 33)

# To get Sue Taleb's age:
age_of_patient = pid4343.age
# To display it:
print(pid4343.age)