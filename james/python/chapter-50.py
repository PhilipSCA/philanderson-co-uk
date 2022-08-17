# Wednesday 17/8/22
#   Functions with functions

# You can call a function within a function
def function1():
    x = "Hi"
    print(x)

# Or you can break it into 2 functions
def calling_function():
    print(x)

def function2():
    x = "Hi"
    calling_function()

# This is an error because x isnt recognised inside the calling_function function. Its a local scope.
# You pass the value of function2's x variable to calling_function as an argument
# calling_function has to recieve it as a parameter.

def calling_function(content):
    print(content)

def function2():
    x = "Hi"
    calling_function(x)


