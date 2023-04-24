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
