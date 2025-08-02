"""Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old."""

import datetime

# Asking the user for their information
while True:
    name = input("What's your name?:")
    if name.replace(" ", "").isalpha() and name.isprintable():
        break
    else:
        print("Incorrect input")

while True:
    try:
        age = int(input("How old are you?:"))
        if age <= 0:
            print("Age can't be less than 0")
            continue
    except:
        print("Incorrect input")
    else:
        break

# Subtracting the user's age from 100 to find how many years are left
difference = 100 - age

# Getting the current date
x = datetime.datetime.now()

# Adding the difference to the current year to find the year they turn 100
turnHundred = x.year + difference

# Final message
print(f"Hi {name}, you are {age} years old, and you will turn 100 years old in the year {turnHundred}.")