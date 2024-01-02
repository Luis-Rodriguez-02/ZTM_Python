# FIND DUPLICATES IN A LIST
# PRINT THE DUPLICATE VALUES

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicate_list = []

# loop through the list and compare the first value i, with the values after it j
# if the value is not already in duplicate_list -> append it to the duplicate list
# do not compare when i and j are the same index because it would compare against itself
for i in range(0, len(some_list)):
    for j in range(1, len(some_list)):
        if some_list[i] == some_list[j] and some_list[i] not in duplicate_list and i != j:
            duplicate_list.append(some_list[i])


print(duplicate_list)