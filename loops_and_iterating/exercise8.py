my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

result = { name: len(name)
           for name in my_set
           if len(name) % 2 != 0 }
print(result)
# {'Cheddar': 7, 'Pudding': 7, 'Cocoa': 5}