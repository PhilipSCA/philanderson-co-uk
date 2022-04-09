# Saturday 9/4/22
    # if statements nested

x = "a"
y = "b"
a = "c"
b = "d"
c = "e"
e = "f"
d = "g"
h = "h"
f = "e"

if (x == y or a == b) and c == d:
    g = h
else:
    e = f

# Another way to write this is using nesting
if c == d:
    if x == y:
        g = h
    elif a == b:
        g = h
    else:
        e = f
else:
    e = f

# If the first line if is true, the next 6 lines execute.
# If the first line is false, the next 6 lines are skipped.
