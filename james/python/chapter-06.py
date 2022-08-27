print ('python - Chapter 6 - Unfamiliar math operators')
print ('==============================================')
print('8 April 2022')

print (' modulo operator (percent symbol) gives you remainder after division')

x = 15
y = 4

modulo_remainder = x % y

print('The remainder of ' + str(x) + " % " + str(y) + ' = ' + str(modulo_remainder))

a = 16
b = 4
c = 16 % 4
print(str(a) + " % " + str(b) + " = " + str(c))
print("When there is no remainder, its assigned 0")




# Addition (this is 4):
age = 3
age = age + 1
# or 
age2 = 3 
age2 += 1

# It is the same as Addition for subtraction and multiplication just use -/* instead of +
# You can add variables

age3 = 5
amount_to_increment = 4
total = age3 + amount_to_increment # = 9
print(str(age3) + ' + ' + str(amount_to_increment) + " = " + str(total))
print("This is 2 variables being added together to make 9")