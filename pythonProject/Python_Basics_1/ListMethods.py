# List Methods
# Remember the Methods and Functions for Strings and Numbers, now we have for lists
basket = [1, 2, 3, 4, 5]
print(len(basket))  # Number of items in list

# Adding to a list
# appends an object to end of list
new_list = basket.append(100)  # The append doesnt make a new list it just adds to the list because they are mutable, append doesnt return anything so None is shown
print(basket)
print(new_list)

# Insert method
basket.insert(2, 600)
print(basket)

# Extend method -> takes an iterable -> something you can loop over
extension_to_list = [700, 800, 900]
basket.extend(extension_to_list)
print(basket)

# pop and remove method
basket.pop() # Removes the last element of the list
print(basket)
basket.pop(0)  # Removes element at specified index
print(basket)  # Pop also returns the value that was removed

basket.remove(800)  # Give the value you want to remove, vs pop give specific index
print(basket)
basket.remove(700)

# Clear
basket.clear()
print(basket)  # Completely empties the list





