# Wednesday 17/8/22
#   Local vs Global variables

# There is Global scope and Local scope
# A global variable is one you define in the main body
x = "Hi"

# A local variable is in a function
def variable():
    y = "Hi"
y = "Hi"
# A global variable is recognised anywhere in your code
# If i did:
print(y)
# Python doesnt recognise it, you get an error message
# but
print(x)
# Python recognises

# If you write the print statement in the function, it recognises them
def z(a, b):
    total = a + b
    print(a)
    print(b)
    print(total)

# If this happens
def x_2():
    y = 2
    print(y)

y = 1
x_2()
print(y)

# On line 30 it displays 2, on line 34 it displays 1