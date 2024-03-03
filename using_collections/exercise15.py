pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

keys = pets.keys()
del pets['Dog']
pets['Snake'] = 'Sssss'
print(keys)

# delete dog key and insert "snake" key