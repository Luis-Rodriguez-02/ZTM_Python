# Lists -> ordered sequence of objects of any type

li = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c']
li3 = [1, 2.6, 'a', True]

amazon_cart = ['notebooks',
               'sunglasses',
               'toys',
               'grapes'
               ]

print(amazon_cart[0])
print(amazon_cart[::-1])  # Remember string slicing

# Data Structures -> Way to organize different data -> container

# List Slicing -> Continuation

print(amazon_cart[0::2])

# Lists are mutable -> list slicing creates a new copy of the list
amazon_cart[0] = 'Laptop'
new_cart = amazon_cart  # This changes the reference of the list to amazon cart and this causes them to share values
print(amazon_cart)

# To copy a list without changing original -> new_list = old_list[:]

