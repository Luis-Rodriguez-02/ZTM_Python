# Dictionary -> Map or HashMap

# This is a data structure, containers around data
dictionary = {
    'a': [1, 2, 3],
    'b': True,
    'x': 'Hello'
}
print(dictionary['b']) # Finds where this is stored at the key of the Map
print(dictionary['x'])  # Error - > non-existent
print(dictionary)
print(dictionary['a'][2])
# Dictionaries are unordered -> values are all over in memory unlike lists

my_list = [{'a': [1, 2, 3], 'b': True, 'x': 'Hello'}]
print(my_list[0]['a'][1])

# Dictionary Keys -> Continued on Dictionaries

# Dictionary Keys -> Must be immutable, the values cannot be changed
# This is why we couldn't use something like a list
# A key in a dictionary must be unique -> if you use same key first one is overridden

# Dictionary Methods
user = {
    'basket': [1, 2, 3],
    'greet': 'hello'
}

# print(user['age'])  # causes error because key doesn't exist; better method:
print(user.get('age'))
print(user.get('age', 55))  # In case age doesn't exist add a default value
print(user)

user2 = dict(name='Luis')
print(user2)

# Dictionary Methods 2

print('basket' in user)  # Does this exist in that


# Keys
print('age' in user.keys())  # checks if this exists in keys of map
print('hello' in user.values())  # checks if this exists in values of map
print('hello' in user.items())  # grabs the whole thing -> 'greet': 'hello'

print(user.items())


# Clear method
user.clear()  # Removes all items in dictionary

# Copy method -> Copies dict
user2 = user.copy()
print(user2)

# Pop / popitem method -> returns value of what was removed
user2.pop('age')
user2.popitem()  # Randomly removes an item


# Update -> Updates key value
user2.update({'ages':55})  # -> if it doesn't exist add item instead


