foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)

# it just prints bar bc we're not calling the function, just printing the variable foo defined at the top. 