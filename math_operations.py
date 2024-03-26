# Basic puthon concepts
#Variables
x = 5
y = 3.14
name = "Alice"

# Data Types
print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'float'>
print(type(name))  # Output: <class 'str'>

# Basic Operators
a = 10
b = 3

print(a + b)  # Addition, Output: 13
print(a - b)  # Subtraction, Output: 7
print(a * b)  # Multiplication, Output: 30
print(a / b)  # Division, Output: 3.3333333333333335
print(a // b) # Integer Division, Output: 3
print(a % b)  # Modulus, Output: 1
print(a ** b) # Exponentiation, Output: 1000

#loops
#if, elif, else
z = 10

if z > 0:
    print("Positive")
elif z == 0:
    print("Zero")
else:
    print("Negative")

# for loop
# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterating over a range
for i in range(5):
    print(i)
    
# while loop
# Print numbers from 1 to 5 using a while loop
i = 1
while i <= 5:
    print(i)
    i += 1
