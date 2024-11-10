my_dict = {'Alex': 1989, 'Andy': 1990}
print(my_dict)
my_dict['Anton'] = 1991
print(my_dict['Alex'],my_dict['Anton'])
my_dict['Slava'] = 1992
print(my_dict['Slava'])
my_dict['Igor'] = 1993
print(my_dict['Igor'])
del my_dict['Andy']
print(my_dict.get('Andy'))
print(my_dict)

my_set = {1,1,2,2,2,3,3,3,3,'one','two','two','three', True, False}
print(my_set)
print(my_set.add('hood'))
print(my_set.add(45))
print(my_set.discard(1))
print(my_set)

