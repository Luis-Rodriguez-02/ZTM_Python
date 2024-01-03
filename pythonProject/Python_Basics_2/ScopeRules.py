# Scope what variables do we have access to

a = 1  # global variable


def parent():
    a = 10  # not a global variable

    def confusion():  # function scope
        return a
    return confusion()


print(a)  # global variable printed
print(parent())  # function variable printed

# 1 - start with local scope
# 2 - is there a parent local scope -> in this case global scope, and parent
# 3 - global scope
# 4 - built in python functions