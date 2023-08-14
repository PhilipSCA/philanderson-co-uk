#14/08/23 17 lines

def my_function():
    print("This is my function")

my_function()

def afunction(fname):
    print(fname + " Anderson")

afunction("James")
afunction("Philip")
afunction("John")

def function1(fname, lname):
    print(fname + " " + lname)

function1("Christa", "Anderson")

def function2(*kids):
    print("The youngest child is " + kids[1])

function2("James", "Hannah", "John")

def function3(child1, child2, child3):
    print("The oldest child is " + child3)

function3(child1 = "Hannah", child2 = "John", child3 = "Philippa")

'''
This is my function
James Anderson
Philip Anderson
John Anderson
Christa Anderson
The youngest child is Hannah
The oldest child is Philippa
'''