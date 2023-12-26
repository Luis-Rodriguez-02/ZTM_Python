print(len('123456789'))  #Length starts from one

greet = "Hellooooo"
print(greet[0:len(greet)])

# Methods use the dot format, functions do not -> they take in values
quote = 'to be or not to be'

print(quote.upper())
print(quote.lower())
print(quote.capitalize())
print(quote.replace("be", 'me'))
print(quote)

# these do not change the string they just make a new one that is discarded after we finish using