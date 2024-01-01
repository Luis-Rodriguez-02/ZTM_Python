# enumerate() -> another useful function
# wrap around an iterable object to turn into an enumerable object

for i, char in enumerate('Zero to Mastery'):
    print(i , char)

# useful if you need an index counter for the item you are looping through


# exercise -> want to create a script that enumerates a list of num 1-10
for index, num in enumerate(list(range(100))):
    if(num == 50):
        print(f'Index of the number 50 is {index}')
    print(index, num)