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

