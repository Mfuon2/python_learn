# Functions
def greet_user(name, age):
    print(f"Name: {name} Age {age}")


# positional arguments and key word argument
greet_user(name="Mfuon", age=13)
greet_user("Mfuon", 13)


# return statements
def square(number):
    return number * number


print(square(3))