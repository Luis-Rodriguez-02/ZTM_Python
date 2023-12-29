# Sets
# Unordered collections of unique objects

my_set = {1, 2, 3, 4, 5}  # Only returns unique items
my_set.add(5)
my_set.add(100)
print(my_set)

my_list = [1, 2, 3, 4, 5, 5]
his_list = [1, 2, 3, 4, 5]
print(set(my_list))

# Set objects don't support indexing, must grab by the item using the in keyword
print(1 in my_set)
print(len(my_set))

print(list(my_set))
new_set = my_set.copy()

# Sets 2

my_own = {1, 2, 3, 4, 5}
your_own = {4, 5, 6, 7, 8, 9, 10}

# difference
print(my_own.difference(your_own))  # duplicates ignored, only shows differences between sets

# discard
my_own.discard(5)  # removes a specified element from the set

# difference_update
my_own.difference_update(your_own)  # updates the set with removal of duplicates

# intersection
my_own.intersection(your_own)  # shares the values they have in common
# my_own & your_own

# isdisjoint
my_own.isdisjoint(your_own)  # returns if the sets have anything in common, are the circles overlapping

# issubset
my_own.issubset(your_own)  # are the values of my set inside the other set -> returns bool

# issuperset
my_own.issuperset(your_own)  # Returns if the set encompasses the other set

# union
my_own.union(your_own)  # combines the sets without duplicates, returns a new set
# my_set | your_set -> shorthand for union

