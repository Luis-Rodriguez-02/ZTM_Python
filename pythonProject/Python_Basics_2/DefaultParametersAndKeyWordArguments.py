# positional arguments
# def foo(first argument, second argument)

# key word arguments
# no need to worry about position

def say_hello(name='name', emoji='emoji'):
    print(f'Hello, {name}! {emoji}')


# generally bad practice because can confuse others
say_hello(emoji='🤡', name='Luis')

# Default parameters
say_hello()  # no arguments given will run the default


