# Exceptions
try:
    age = int(input('Age : '))
    print(age)
    age = 2/age
except ZeroDivisionError:
    print('Age cannot be Zero')
except ValueError:
    print('Invalid Number')