#Strings in Python!

'hi hello there'  # this is a string
"hello"  # this is also a string

print("Hello")
user_name = 'supercoder'
password = 'supersecret'

long_string  = '''
WOW THIS IS A VERRY LONG STRING
O O
---
'''

print(long_string)

first_name = 'Luis'
last_name = 'Rodriguez'
full_name = first_name + " " + last_name
print(full_name)

# String concatenation
# Adding strings

print('hello ' + ' Luis')
# print('hello' + 5)  # gives type error, must be with strings

# Type conversion

print(type(str(100))) # String
print(type(int(str(100)))) # Integer

# Above is the same as doing this -> type conversion
a = str(100)
b = int(a)
c = type(b)
print(c)


