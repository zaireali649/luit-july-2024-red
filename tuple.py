# Initialize an empty list
list1 = []

# Create a tuple with multiple elements
tuple1 = ('Happy', 'Sad', 'Excited', 'Nervous', 'Calm')

# Print the type of tuple1, which should be <class 'tuple'>
print("Type of tuple1:", type(tuple1))

# Accessing elements in a tuple by index
print("First element of tuple:", tuple1[0])  # 'Happy'
print("Last element of tuple:", tuple1[-1])  # 'Calm'

# Slicing a tuple (getting a subtuple)
subtuple = tuple1[1:4]  # From index 1 to 3 (not including 4)
print("Sliced tuple:", subtuple)  # ('Sad', 'Excited', 'Nervous')

# Unpacking a tuple into variables
mood1, mood2, mood3, mood4, mood5 = tuple1
print("Unpacked moods:", mood1, mood2, mood3, mood4, mood5)

# Convert the tuple to a list
list1 = list(tuple1)
print("List converted from tuple:", list1)

# Adding elements to the list
list1.append('Anxious')  # Append an element at the end
print("List after appending 'Anxious':", list1)

# Extending the list with another list
list1.extend(['Joyful', 'Angry'])
print("List after extending with ['Joyful', 'Angry']:", list1)

# Inserting an element at a specific position
list1.insert(2, 'Surprised')  # Insert 'Surprised' at index 2
print("List after inserting 'Surprised' at index 2:", list1)

# Removing elements from the list
list1.remove('Sad')  # Remove the first occurrence of 'Sad'
print("List after removing 'Sad':", list1)

# Popping elements from the list
popped_element = list1.pop()  # Remove and return the last element
print("Popped element:", popped_element)
print("List after popping the last element:", list1)

# Reversing the list
list1.reverse()
print("Reversed list:", list1)

# Sorting the list (in-place sort)
list1.sort()
print("Sorted list:", list1)

# Create a new sorted version of the list (without changing the original list)
sorted_list = sorted(list1, reverse=True)
print("New sorted list in descending order:", sorted_list)
print("Original list remains unchanged:", list1)

# Count occurrences of an element in the list
happy_count = list1.count('Happy')
print("Number of times 'Happy' appears in the list:", happy_count)

# Finding the index of an element
excited_index = list1.index('Excited')
print("Index of 'Excited' in the list:", excited_index)
