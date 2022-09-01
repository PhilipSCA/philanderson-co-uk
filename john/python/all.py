print("all projects")
print("============")

def chapter_53():
    print("Classes Friday 26/08/22")
    print("===========================")
    print("creating patients using Patient Class")
    print("")

    class Patient():
        def __init__(self, last_name):
            self.last_name = last_name

    import json

    pid4343 = '{"last_name": "Taleb"}'
    x = json.loads(pid4343)
    pid4344 = {"last_name": "Anand"}
    pid4345 = {"last_name": "Lin"}
    pid1298 = {"last_name": "Nilsson"}

    print("Patient 4343's last name is " + str(x["last_name"]))
    print("Patient 4344's last name is " + pid4344["last_name"])
    print("Patient 4345's last name is " + pid4345["last_name"])
    print("Patient 1298's last name is " + pid1298["last_name"])
    print(" ")

#==================================================================================

def chapter_54():
    print("Classes Friday 26/08/22")
    print("===========================")
    print("creating patients using Patient Class")
    print("")

    class Patient():
        def __init__(self, last_name):
            self.last_name = last_name

    import json

    pid4343 = '{"last_name": "Taleb"}'
    x = json.loads(pid4343)
    pid4344 = {"last_name": "Anand"}
    pid4345 = {"last_name": "Lin"}
    pid1298 = {"last_name": "Nilsson"}

    print("Patient 4343's last name is " + str(x["last_name"]))
    print("Patient 4344's last name is " + pid4344["last_name"])
    print("Patient 4345's last name is " + pid4345["last_name"])
    print("Patient 1298's last name is " + pid1298["last_name"])
    print(" ")
    
#======================================================================================

def chapter_55():
    print("Classes Friday 26/08/22")
    print("===========================")
    print("creating patients using Patient Class")
    print("")

    class Patient():
        def __init__(self, last_name):
            self.last_name = last_name

    import json

    pid4343 = '{"last_name": "Taleb"}'
    x = json.loads(pid4343)
    pid4344 = {"last_name": "Anand"}
    pid4345 = {"last_name": "Lin"}
    pid1298 = {"last_name": "Nilsson"}

    print("Patient 4343's last name is " + str(x["last_name"]))
    print("Patient 4344's last name is " + pid4344["last_name"])
    print("Patient 4345's last name is " + pid4345["last_name"])
    print("Patient 1298's last name is " + pid1298["last_name"])
    print(" ")

#============================================================================================

def chapter_56():
    print("Classes Friday 26/08/22")
    print("===========================")
    print("creating patients using Patient Class")
    print("")

    class Patient():
        def __init__(self, last_name):
            self.last_name = last_name

    import json

    pid4343 = '{"last_name": "Taleb"}'
    x = json.loads(pid4343)
    pid4344 = {"last_name": "Anand"}
    pid4345 = {"last_name": "Lin"}
    pid1298 = {"last_name": "Nilsson"}

    print("Patient 4343's last name is " + str(x["last_name"]))
    print("Patient 4344's last name is " + pid4344["last_name"])
    print("Patient 4345's last name is " + pid4345["last_name"])
    print("Patient 1298's last name is " + pid1298["last_name"])
    print(" ")

#=============================================================================

def chapter_57():
    print("Classes Friday 26/08/22")
    print("===========================")
    print("creating patients using Patient Class")
    print("")
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
    print("age of patient is " + str(age_of_patient))

    print(f"First patient - {pid4343.first_name} {pid4343.last_name}, age {pid4343.age}") 
    print(f"Second patient - {pid4344.first_name} {pid4344.last_name}, age {pid4344.age}")
    print(f"Third patient - {pid4345.first_name} {pid4345.last_name}, age {pid4345.age}")
    print(f"Fourth patient - {pid1298.first_name} {pid1298.last_name}, age {pid1298.age}")
    print(" ")

#=======================================================================================================

def chapter_58():
    print("Classes Friday 26/08/22")
    print("===========================")
    print("creating patients using Patient Class")
    print("")

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
    print("age of patient is " + str(age_of_patient))

    print(f"First patient - {pid4343.first_name} {pid4343.last_name}, age {pid4343.age}") 
    print(f"Second patient - {pid4344.first_name} {pid4344.last_name}, age {pid4344.age}")
    print(f"Third patient - {pid4345.first_name} {pid4345.last_name}, age {pid4345.age}")
    print(f"Fourth patient - {pid1298.first_name} {pid1298.last_name}, age {pid1298.age}")
    print(" ")

#=============================================================================================================================================================================================================================================


user_input = ""
while user_input != "q":
  user_input = input("Enter a chapter, or q to quit:")
  print(f"chapter {user_input}:")

  if user_input != "q":

    if user_input == "53":
        chapter_53()
    
    if user_input == "54":
        chapter_54()

    if user_input == "55":
        chapter_55()
    
    if user_input == "56":
        chapter_56()

    if user_input == "57":
        chapter_57()

    if user_input == "58":
        chapter_58()
