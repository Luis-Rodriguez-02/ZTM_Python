# FIND DUPLICATES IN A LIST
# PRINT THE DUPLICATE VALUES
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicate_list = []
duplicate_list2 = []

# loop through the list and compare the first value i, with the values after it j
# if the value is not already in duplicate_list -> append it to the duplicate list
# do not compare when i and j are the same index because it would compare against itself
for i in range(0, len(some_list)):
    for j in range(1, len(some_list)):
        if some_list[i] == some_list[j] and some_list[i] not in duplicate_list and i != j:
            duplicate_list.append(some_list[i])

# another solution using .count() method, the method returns how many times the value occurs in the list
for value in some_list:
    if some_list.count(value) > 1 and value not in duplicate_list2:
        duplicate_list2.append(value)


print(duplicate_list)
print(duplicate_list2)