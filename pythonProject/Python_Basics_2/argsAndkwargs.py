# *args **kwargs

def super_func(*args, **kwargs):
    total = 0
    print(args)  # gives a tuple of the arguments
    print(kwargs)  # gives a dictionary of the key word arguments
    for items in kwargs.values():
        total += items
    return sum(args) + total


# *args -> can accept any number of positional arguments
print(super_func(1, 2, 3, 4, 5, num1=5, num2=10))


# rule -> params, *args, default params, **kwargs

def test_func(name, *args, test='hi', **kwargs):
    pass
