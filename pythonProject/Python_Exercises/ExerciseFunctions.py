# make a function that gives you the highest even number from a list

def highest_even(li):
    highest = 0
    for value in range(len(li)):
        if li[value] > highest and li[value] % 2 == 0:
            highest = li[value]
    return highest


# another way using max(iterable)
def highest_even_two(lis):
    highest = 0
    even = []
    for item in lis:
        if item % 2 == 0:
            even.append(item)
    return max(even)


nums = [2, 4, 6, 8, 92]
print(highest_even(nums))
print(highest_even_two(nums))
