# List of spendings in dollars
spendings = [32.45, 18.65, 23.45, 78.32, 5.23]

# Initialize a variable to store the total sum of spendings
total_sum = 0.0

# Loop through each spending in the list
for spending in spendings:
    total_sum += spending  # Add each spending amount to the total sum
    # Print the cumulative money spent so far, formatted to 2 decimal places
    print('Money spent so far: $', format(total_sum, '.2f'))

# Calculate and print the total amount of money spent
print('Total money spent: $', format(total_sum, '.2f'))

# Calculate the average spending
average_spending = total_sum / len(spendings)
print('Average spending: $', format(average_spending, '.2f'))

# Find and print the maximum and minimum spending amounts
max_spending = max(spendings)
min_spending = min(spendings)
print('Maximum spending: $', format(max_spending, '.2f'))
print('Minimum spending: $', format(min_spending, '.2f'))

# Finding the number of transactions that exceed a specific threshold
threshold = 20.00
high_spendings = [s for s in spendings if s > threshold]
print('Number of transactions over $20:', len(high_spendings))
