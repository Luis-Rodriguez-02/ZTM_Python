#Convert input into stars and to print it in formatted string

user_name = input("Enter your username: \n")
password = input("Enter your password: \n")

password_length = len(password)
hidden_password = '*' * password_length

print(f'{user_name}, your password {hidden_password} is {password_length} letters long')