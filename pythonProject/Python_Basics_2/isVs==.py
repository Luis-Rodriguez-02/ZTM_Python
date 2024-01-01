print(True == 1)  # True
print('' == 1)  # False
print([] == 1)  # False
print(10 == 10.0)  # False -> I was wrong its True
print([] == [])   # True

# is -> Python keyword
# Checks if the location in memory is the same.
# Checks for the exact thing vs == checks for values
print(True is True)
print([] is [])  # false because lists are objects -> two different lists
print('i' is 'i')

a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)  # false
# versus
print(a == b)  # true
