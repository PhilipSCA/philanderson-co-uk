# Wednesday 24/8/22
#   More on building a class

# We need there to be a variable that has the same value as the attribute, last_name
# It can be any name you like as long as its legal
class patient():
    def __init__(self, last_name):
        self.x = last_name

# But for now we are going to just use last_name as its easier
class Patient():
    def __init__(self, last_name):
        self.last_name = last_name