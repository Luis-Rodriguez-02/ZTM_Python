# build a counter
# counts the items in a list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
sum_nums = 0

for i in my_list:
    sum_nums += i
    count += 1
print(f'There are {count} numbers in the list and the sum is equal to {sum_nums}')

