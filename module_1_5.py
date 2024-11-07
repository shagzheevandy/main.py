immutable_var = 1, 2 ,3, True, 'my dream'
print(immutable_var)
# кортежи неизменяемые объекты, но в случае наличия в кортеже списка как одного из объектов кортежа,
# именно его можно изменить, так как списки изменяемы
# например
immutable_var = (1, ['i', 'you', 'we'])
print(immutable_var)
immutable_var[1][1] = 'he'
print(immutable_var)

mutable_list = ['if', 'you', 'had', 'one', 'moment...']
print(mutable_list)
mutable_list[-1] = 'chance...'
print(mutable_list)
mutable_list[0] = 'would'
mutable_list[2] = 'capture'
mutable_list[3] = 'it'
mutable_list[4] = 'or let it slip???'
print(mutable_list)
