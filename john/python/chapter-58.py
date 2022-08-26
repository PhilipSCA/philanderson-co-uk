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


print(pid4343)
print(pid4344)
print(pid4345)
print(pid1298)

print("First patient - Name - " + str(pid4343.first_name) + " " + str(pid4343.last_name) + ", age " + str(pid4343.age)) 
print("Second patient - Name - " + str(pid4344.first_name) + " " + str(pid4344.last_name) + ", age " + str(pid4344.age))
print("Third patient - Name - " + str(pid4345.first_name) + " " + str(pid4345.last_name) + ", age " + str(pid4345.age))
print("Fourth patient - Name - " + str(pid1298.first_name) + " " + str(pid1298.last_name) + ", age " + str(pid1298.age))   


