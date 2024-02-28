def foo(first, second=3, third=2): # when you see # in a function it means it has a default argument
    print(first)
    print(second)
    print(third)

foo(42, 3.141592, 2.718)

# print a list of the numbers in the parameters, second and third get reassigned.