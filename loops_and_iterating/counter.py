counter = 1
while counter <= 1000:
    print(counter)
    counter += 1

#or 
    
names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []

for name in names:
    upper_name = name.upper()
    upper_names.append(upper_name)
    # Deleted: index += 1

print(upper_names)
# ['CHRIS', 'MAX', 'KARIS', 'VICTOR']