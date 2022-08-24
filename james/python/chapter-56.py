# Wednesday 24/8/22
#   Creating an instance

class Patient():
    def __init__(self, last_name):
        self.last_name = last_name

# The only thing that differs in the form is what the patients put in.
# Each sheet has a unique identifier automatically when printed.
# This sheets patient ID (unique identifier) is james28
# To fill in the blank part, we do this
james28 = Patient("Anderson")

# james28 is just a variable, but each patient must have a different identifier.
# We can use the class to make as many instances as we need.
james28 = Patient("Anderson")
james29 = Patient("Smith")
james30 = Patient("Billet")
james31 = Patient("Coles")

# Or you could create a dictionary
james28 = {"last name": "Anderson"}
james29 = {"last name": "Smith"}
james30 = {"last name": "Billet"}
james31 = {"last name": "Coles"}
james54 = {"last name": "Ellis"}