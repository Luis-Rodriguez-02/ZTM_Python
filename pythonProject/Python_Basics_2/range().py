# range() -> function that produces a sequence of integers from start to stoo

print(range(100))  # -> not a tuple, it's a range object.

for number in range(0, 100, 2):  # third parameter -> step over like lists
    print(number)

# can go in reverse
for _ in range(10, 0, -1):  # -> starts from 10 to 0
    print(_)

# can do this
print(list(range(10)))  # this is a good way to turn items into a list
