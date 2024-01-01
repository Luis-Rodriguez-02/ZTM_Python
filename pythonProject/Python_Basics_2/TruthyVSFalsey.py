# Truthy and Falsy

is_old = bool('hello')
is_licenced = bool(5)

print(bool('hello'))  # Truthy values
print(bool(5))


print(bool(0))  # Falsy values
print(bool(None))

password = None
username = ''

if password and username:
    print("Inputs have been provided")
else:
    print("No input provided")
