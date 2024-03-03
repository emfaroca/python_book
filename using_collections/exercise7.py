# Write Python code to replace all the : characters in the string below with +

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

info = 'xyz:*:42:441:Lee Kim:/home/xyz:/bin/zsh'
parts = info.split(':')
result = '+'.join(parts)
print(result)

# or 

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
result = info.replace(':', '+')
print(result)
