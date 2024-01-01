# while condition : do something
i = 0
while i <= 50:
    print(i)
    i += 1
else:
    print('Done with all the work')  # only executes if while turns false

# while -> part 2
my_list = [1, 2, 3]
for item in my_list:
    print(item)

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

while True:
    response = input("Say something")
    if response == 'bye':
        break
