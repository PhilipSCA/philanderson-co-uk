# Wednesday 24/8/22
#   A more complex class

# This is a class with a single attribute: last_name
class Patient():
    def __init__(self, last_name):
        self.last_name = last_name

# With instantiated classes 5 times
james28 = Patient("Anderson")
james29 = Patient("Smith")
james30 = Patient("Billet")
james31 = Patient("Coles")
james54 = Patient("Ellis")

# We are going to add 2 more attributes
class Patient():
    def __init__(self, last_name, first_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

james28 = Patient("Anderson, James, 14")
james29 = Patient("Smith, John, 14")
james30 = Patient("Billet, Philip, 17")
james31 = Patient("Coles, Hannah, 11")
james54 = Patient("Ellis, Christa, 19")

# These work like positional arguments, last_name is assigned "Anderson" for james28
