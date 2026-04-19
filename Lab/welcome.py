a = "Hello"
b = "World!"
print(a + " " + b)

print(id(a), " -- ", id(b)) 

a=0.1+0.2
b = 0.3
print(a, " ", b)

print(a == b)

import math
print(a==b)
print(math.isclose(a, b))

help("modules")

# mutable vs immutable
a = [1, 2, 3]
b = a
print(id(a), " -- ", id(b))

a.append(4)
print(a, " ", b)

print(type(3.14))

print(type("Hello World!"))

# age comparison
age = 25
if age < 18:
    print("You are a minor.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")  


# logical operators
is_student = True
if age >= 18 and is_student:
    print("You are an adult student.")
else:
    print("You are not an adult student.")


# loops
for i in range(5):
    print(i)

for i in range(10, 0, -1):
    print(i)

    print("Liftoff!")


def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count