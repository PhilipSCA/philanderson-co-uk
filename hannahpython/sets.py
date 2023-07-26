myset = {"a", "b", "c"}
print(myset)
#set items are unordered so they can come in any way

set1 = set(("d", "a", "b", "m", "e"))
print(set1)


set2 = {"apple", "banana", "cherry"}
print("cherry" in set2)


set3 = {"l", "o", "p"}
set3.add("r")

print(set3)


set4 = {"y", "e", "s"}
set5 = {"n", "o", "p"}

set4.update(set5)
print(set4)


set6 = {"apple", "banana", "cherry"}
x = set6.pop()

print(x)
print(set6)

z = {"bing", "android", "samsung"}
p = {"google", "yahoo", "bing"}

z.intersection_update(p)
print(z) #keep items present in both sets (bing)