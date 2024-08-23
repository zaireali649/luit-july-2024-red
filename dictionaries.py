# Initialize an empty list
list1 = []

# Create a dictionary with multiple mood elements
moods_dict = {
    0: 'Happy',
    1: 'Sad',
    2: 'Excited',
    3: 'Nervous',
    4: 'Calm'
}

# Print the type of moods_dict, which should be <class 'dict'>
print("Type of moods_dict:", type(moods_dict))

# Accessing elements in a dictionary by key (simulating index access)
print("First element of dictionary:", moods_dict[0])  # 'Happy'
print("Last element of dictionary:", moods_dict[4])  # 'Calm'

# Slicing equivalent: Get a sub-dictionary (mimicking tuple slicing)
subdict = {k: moods_dict[k] for k in range(1, 4)}  # From keys 1 to 3
print("Sliced dictionary:", subdict)  # {1: 'Sad', 2: 'Excited', 3: 'Nervous'}

# Unpacking a dictionary into variables (simulating tuple unpacking)
mood1, mood2, mood3, mood4, mood5 = moods_dict.values()
print("Unpacked moods:", mood1, mood2, mood3, mood4, mood5)

# Convert the dictionary values to a list
list1 = list(moods_dict.values())
print("List converted from dictionary values:", list1)

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
