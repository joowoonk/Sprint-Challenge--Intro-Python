# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = []
aa = []

for i in humans:
    a.append(i.name)
for d in range(len(a)):
    if a[d][0].lower() == "d":
        aa.append(a[d])

print(aa)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = []
bb = []

for i in humans:
    b.append(i.name)
for e in range(len(b)):
    if b[e][-1].lower() == "e":
        bb.append(b[e])

print(bb)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = []
cc= []

for i in humans:
    c.append(i.name)
for letter in range(len(c)):
    if c[letter][0].lower() == "c" or c[letter][0].lower()== "d" or c[letter][0].lower() == "e" or c[letter][0].lower() == "f" or c[letter][0].lower() == "g":
        cc.append(c[letter])
print(cc)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = []
for number in humans:
    d.append(number.age+10)
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = []
for both in humans:
    e.append(f"{both.name}-{both.age}")
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = []

for c, value in enumerate(humans):
    if value.age > 27 and value.age < 32:
        f.append((value.name, value.age))
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = []

for i in humans:
    g.append(f"{i.name.upper()},{i.age + 5}")
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = []

for i in humans:
    h.append(f"{i.name}, {math.sqrt(i.age)}")
print(h)
