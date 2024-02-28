def set_foo():
    foo = 'bar'

set_foo()
print(foo)


# you get an error because foo is part of the function body, it's not defined. It isn't in scope