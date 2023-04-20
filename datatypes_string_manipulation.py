
price = 10  # decimal system converted to binary

# Common datatypes
p = 10  # int
rating = 4.0  # Float
is_published = False  # Booleans
name = 'Mfuon Leonard'  # Strings

# Complex datatypes

# full_name = input('What is your Name : ')
# fav_color = input('Favorite color : ')
# text = full_name + ' likes ' + fav_color
# print(text)

course = 'Python for beginners'
# using strings with range
print(course[1:])  # from index 1 to the end of the string
print(course[1:3])  # between a range provided
print(course[:5])  # From 0 to index 5
print(course[:])  # assumed 0 to be the start of the index and length of the string to be the end

# Formatted string prefixed with an f
first_name = 'Mfuon'
last_name = 'Leonard'
msg = f'{first_name} [{last_name}] is a Software Engineer'
print(msg)

# String Methods
course = 'Python for beginners'
print(len(course))  # Length of string
print(course.upper())  # convert to UpperCase
print(course.lower())  # convert to LowerCase
print(course.find('P'))  # find the index of character P
print(course.replace('beginners', 'Absolute beginners'))  # replace a string with another
print('Py' in course)  # returns is a sequence of characters exists in a string (
print(course.title())  # title case for a string