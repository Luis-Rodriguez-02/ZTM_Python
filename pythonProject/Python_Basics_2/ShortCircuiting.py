# Short Circuiting

is_friend = True
is_user = True

# Short circuitng can be done when we use something like or
# when we do or if the first condition is true second val is not checked
if True or is_user:
    print(is_friend and is_user)

# Works with and if the first val is false
if False and True:
    print("Never printed and short circuit")
