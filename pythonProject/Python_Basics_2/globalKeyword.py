# Scope continued


a = 10
def confusion(b):  # parameters are considered local scope
    print(b)
    a = 90


confusion(300)


total = 0
def count():
    global total
    total += 1
    return total

def better_count(total):
    total += 1
    return total


print(better_count(better_count(better_count(total))))
# a better way -> dependency injection
# detach the dependency to the global variable
