# Dictionaries

customers = {
    "name": "John",
    "age": 30,
    "is_verified": True
}

# get the value of a dictionary using .get() or []

print(customers.get("name", "Leonard"))  # get the key value or the alternative value

# update a key and value to the dictionary

customers["dob"] = "Jan 2 1922"

print(customers)