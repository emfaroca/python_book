my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]


result = []
for number in my_list:
    if number % 2 == 0:
        result.append('even')
    else:
        result.append('odd')

print(result)