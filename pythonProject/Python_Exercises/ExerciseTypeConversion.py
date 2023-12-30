from datetime import datetime
name = 'Luis'
age = 21
relationship_status = 'Single'

relationship_status = 'It\'s complicated'
print(relationship_status)

birth_year = int(input('What year were you born' + "\n"))
age = datetime.now().year - birth_year # must convert birth_year to int
#Print out a formatted String with input
print(f'Hello {name}, you are {age} years old. Your birth year is {birth_year}')
