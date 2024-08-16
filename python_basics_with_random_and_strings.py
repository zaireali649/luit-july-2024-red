import random  # Import the random module for generating random numbers
import time  # Import the time module for adding delays

number = 33  # Assign the value 33 to the variable 'number'

random_number = random.randint(0, 100)  # Generate a random integer between 0 and 100 and assign it to 'random_number'

# Adding a delay before printing to create suspense
print("Generating a random number between 0 and 100...")
time.sleep(2)  # Pause for 2 seconds

print(f"The static number is {number}, and the random number is {random_number}.")  # Print the values with a formatted string

# Exploring the variable types with additional information
print(f"Type of 'number': {type(number)}")  # Print the data type of 'number'
print(f"Type of 'random_number': {type(random_number)}")  # Print the data type of 'random_number')

var = "This is a sentence."  # Assign a string to the variable 'var'

# Transforming the string in different ways
print(f"Original string: {var}")
print(f"Lowercase: {var.lower()}")  # Print the lowercase version of the string stored in 'var'
print(f"Uppercase: {var.upper()}")  # Print the uppercase version of the string
print(f"Title case: {var.title()}")  # Print the string in title case

# Checking if the string is a digit or an alpha
print(f"Is the string numeric? {var.isdigit()}")  # Check if 'var' is a number
print(f"Is the string alphabetic? {var.isalpha()}")  # Check if 'var' is alphabetic

# Exploring the attributes and methods of a string object
print("\nAttributes and methods associated with the string object 'var':")
print(dir(var))

# Let's also explore some cool methods of the random module
print("\nSome cool methods of the random module:")
print(f"Random floating point number between 0 and 1: {random.random()}")  # Print a random floating point number between 0 and 1
print(f"Random choice from a list: {random.choice(['apple', 'banana', 'cherry'])}")  # Print a random choice from a list

# Shuffling a list for fun
fruit_list = ['apple', 'banana', 'cherry']
random.shuffle(fruit_list)  # Shuffle the list
print(f"Shuffled list: {fruit_list}")
