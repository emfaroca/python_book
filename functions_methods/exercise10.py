def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592)

# print
# 42
# 3.141592
# 2

# didn't give a third parameter so we're printing the default argument
