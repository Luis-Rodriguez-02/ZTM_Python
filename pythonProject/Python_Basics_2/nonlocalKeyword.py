def outer():
    x = 'local'  # local to outer function

    def inner():
        nonlocal x  # refers to parent local
        x = 'nonlocal'  # jumps up to parent scope -> refers to x = 'local', replaced 'local' with 'nonlocal'
        print('inner:', x)
    inner()
    print('outer:', x)


outer()


# try to avoid using these keywords -> make code clean and predictable
