# Wednesday 24/8/22
#   Getting info out of instances   

class Patient():
    def __init__(self, age):
        self.age = age

james28 = Patient("Anderson, James, 14")

# To access James' age, we do this
age_of_patient = james28.age
