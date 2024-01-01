# Iterable
# Object or collection that can be iterated over
# Strings, lists, dictionaries, tuples, sets
# iterated -> one by one check each item in the collection

user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

for item in user.items():  # Returns key-value pairs in a tuple
    print(item)
print('\n')
for item in user.values():  # Returns values of the dictionary
    print(item)
print('\n')
for item in user.keys():  # Returns keys of the dictionary
    print(item)
print('\n')

# printing key value items separately using tuple unpacking
for item in user.items():
    key, value = item
    print(key, value)
print('hello\n')

# shorthand for above ^
for key, value in user.items():
    print(key, value)
