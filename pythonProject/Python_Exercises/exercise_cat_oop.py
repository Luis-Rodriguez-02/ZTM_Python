#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1, cat2, cat3 = Cat('Tom', 2), Cat('Max', 3), Cat('Shelby', 1)


# 2 Create a function that finds the oldest cat
def oldest_cat(*cats):
    oldest = 0
    for cat in cats:
        oldest = cat.age if cat.age > oldest else oldest
    return oldest

cat_list = [cat1, cat2, cat3]
print(oldest_cat(*cat_list))

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'The oldest cat is {oldest_cat(*cat_list)} years old')

