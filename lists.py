# names = ['Q1', 'Q2', 'Q3', 'Q4']
# print(names[:])
# names[2] = 'Mfuon'
# print(names)

# Find the largest number in a list
# 1D Lists

numbers = [1, 3, 4, 5, 1, 5, 9, 2]
largest_number = 0

for number in numbers:
    if number > largest_number:
        largest_number = number

print(largest_number)

# 2D Lists

matrix = [
    [1, 2, 3],
    [1, 4, 5],
    [5, 6, 8]
]

for row in matrix:
    for column in row:
        print(column)

# List functions

# Appends a value to the end of the list
numbers.append(20)  # appends a number at the end
print(numbers)

# inserts a value in a particular index
numbers.insert(0, 89)  # Inserts a value in the mid
print(numbers)

# Removes a specific value in a given list
numbers.remove(89)  # removes a specific item on the list
print(numbers)

# Removes the last value in a list
numbers.pop()  # removes the last element opn the list
print(numbers)

# Prints out the index of the value in a list
print(f'Get index of a value : {numbers.index(9)}')  # this will print the index of the following

# Check if value is in a list
print(f'Is Number exist : {5 in numbers}')  # Checks the availability of 7 in the list

# Counts the existence of values on a list
print(f'Count occurrence: {numbers.count(9)}')  # counts the number of 9ns in the list

# Sort Alist
numbers.sort()  # sorts the list
print(f'Sorted : {numbers}')

# Reverse a list
numbers.reverse()  # reverses the list
print(f'Reversed : {numbers}')

# Copy List to another
numbers2 = numbers.copy()
print(f'Copied list : {numbers2}')

# Clear contents of a list
numbers.clear()  # removes a all elements of a list
print(f'Cleared a list :  {numbers}')

# assessment is to remove duplicates in a list

# using a for loop

items = [8, 90, 8, 3, 9, 1, 0, 2, 4, 2]
clean_list = []

for nums in items:
    if nums not in clean_list:
        clean_list.append(nums)

print(f'Items with duplicates {items}')
print(f'Items without duplicates {clean_list}')

# using sets
items = set(items)
print(f'Removed duplicates withset {items}')
