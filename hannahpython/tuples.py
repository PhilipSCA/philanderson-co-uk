thistuple = ("apple", "banana", "cherry")
print(thistuple)

#=======================================================
thattuple = tuple(("apple", "banana", "cherry"))
print(len(thattuple)) #how many items in that tuple

#=======================================================
mytuple = ("apple",) #need the comma afterwards
print(type(mytuple))

#=======================================================
tuple1 = ("apple", "banana", "cherry") #string
tuple2 = (1, 5, 9, 2, 4)               #interger
tuple3 = (True, False, True)           #boolean

print(tuple1)
print(tuple2)
print(tuple3)

#=======================================================
tuple5 = (True, "tomato", 1, False, 7)
print(tuple5)

#=======================================================
thisstuple = ('apple', 'strawberry', 'lemon')
if 'lemon' in thisstuple:
    print("Yes!, 'Lemon' is in this tuple")
else:
    print("No! 'Lemon' is not in this tuple")

#=======================================================
x = ("apple", "banana", "cherry")
y = list(x)
y[-1] = "lemon"
x = tuple(y)

print(x)

#=======================================================
yestuple = ("apple", "pineapple", "strawberry", "lemon")
y = list(yestuple)
y.append("orange")
yestuple = tuple(y)

print(yestuple)