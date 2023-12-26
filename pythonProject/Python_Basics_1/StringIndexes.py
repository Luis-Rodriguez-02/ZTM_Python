# Strings are ordered sequences of characters
eat = '01234567'

# [start] , or [start:stop] or [start:stop:stepover]
print(eat[0])

# Gets everything up to stop index and omits
print(eat[0:2])
print(eat[0:6])

# Steps over
print(eat[0:6:2])

# Reverse order using stepover
print(eat[::-1])
