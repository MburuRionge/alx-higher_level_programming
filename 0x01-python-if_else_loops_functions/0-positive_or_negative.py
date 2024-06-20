#!/usr/bin/python3

# Generate a random integer between -10 and 10
import random


# Print the number followed by the correct description
number = random.randint(-10, 10)
print(f"{number}", end=" ")
if number > 0:
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")
