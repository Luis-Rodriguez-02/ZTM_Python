# the walrus operator :=

a = 'helloooooooooo'

if (n := len(a)) > 10:  # n = len(a) will not work
    print(f'Too long {n} elements')


while (n := len(a)) > 1:
    print(n)
    a = a[:-1]

print(a)