my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

print(another_list)
# Are the lists assigned to my_list and another_list equal?
#answer: yes

#Are the lists assigned to my_list and another_list the same object?
# no, list creates new object

# Are the nested lists at index 3 of my_list and another_list equal?
# yes

# Are the nested lists at index 3 of my_list and another_list the same object?
# yes, shallow copy