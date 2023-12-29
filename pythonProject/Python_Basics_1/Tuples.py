# Tuple
# Like a list -> but immutable (can't change values)
# If you don't need to change the list use it -> code predictable, less flexible than a list
# Usually faster than list

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[2])
print(5 in my_tuple)

# Tuples 2

new_tuple = my_tuple[:]
print(new_tuple)

x = my_tuple[0]
x, y, z, *other = (5, 5, 9, 10, 11, 200)

print(x)
print(other)


# count and index
print(my_tuple.count(5))
my_tuple.index(5)