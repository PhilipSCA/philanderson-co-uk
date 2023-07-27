thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    #"year": 2020 will overwrite 1964
}
print(thisdict)
#print(thisdict["brand"])

print(len(thisdict))
print(type(thisdict))

dict1 = dict(name = "Hannah", age = "12", country = "England")
print(dict1)

dict2 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = dict2.keys()
print(x)

dict3 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = dict3.keys()
print(x)

dict3['colour'] = 'white'
print(x)

dict4 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = dict4.values()
print(x)

dict5 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = dict5.values()
print(x) #before the change

dict5["year"] = 2020
print(x) #after the change

dict6 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = dict6.items()
print(x)