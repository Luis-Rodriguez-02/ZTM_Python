# functions either modify something or return something
# a function should do something really well
def sum(num1, num2):
    def another_function(n1, n2):
        return n1 + n2

    return another_function(num1, num2)


total = sum(10, 20)

print(total)
