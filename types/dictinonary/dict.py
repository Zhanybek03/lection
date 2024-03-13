# dict_1 = {
#     'brand': 'Ford',
#     'model':  'Mustang', 
#     'year': 1967
# }
# print(dict_1, type(dict_1))
# print(dict_1['brand'], dict_1['model'])
# print(dict_1['year'])
# ls = ['ford', 'Mustang', 1967]
# print(ls,)

# dict_1['motor'] = 'GTI Turbo'
# dict_1['model'] = 'Fiesta'
# print(dict_1['motor'], dict_1['model'])

# ----------------------
# print(dir(dict))

# items , keys, values 
# user_info = {
#     'first_name': 'John',
#     'last_name': 'Snow', 
#     'age': 24,
#     'email': 'bastard123@gmail.com',
#     'role': 'admin',
# }
# print(user_info)

# ls = user_info.keys()
# print(ls)
# ls2 = list(user_info.values())
# print('ls-2',ls2)

# ls3 = list(user_info.items())
# print(ls3[0])
# print('\n Values: ')
# for value in user_info.values():
#     print(value)
# print('\n Keys: ')
# for key in user_info.keys():
#     print(key)

# print(
#     '\n Items:'
# )
# for key, value in user_info.items():
#     print(f'keys:{key} \nvalues: {value}')


# изменение
# dict_ = {
#     "name": 'Alihan',
#     'age': 17
# }
# dict_['age'] = 29
# dict_['name'] = 'John'
# dict_['address'] = "WinterFell"
# dict_.update(age = 24, address = 'BlackCastle')
# dict_.update({'name': 'John Snow'},)
# print(dict_)

# dict_ = {1: 'Pizza', 2: 'Burger', 3: 'Steak'}
# print(dict_[2], '!!!!!')
# print(dict_.get(7, 'Not found!'))

# setdefault = работает так же как get, но если нет такого ключа то создаетт новую пару этого ключа
# dict_ = {1: 'Pizza', 2: 'Burger', 3: 'Steak'}
# print(dict_.setdefault(5,'Manty'))
# print(dict_)


# ------------
# ls = list(range(1, 20))
# new_dict = dict.fromkeys(ls, 'default')
# new_dict[1] = 'Manty'
# print(new_dict)

# -----------------
# deleting elements
# pop, popitem

# pop(<key>) - удаляет пару по ключу
# popitem() - удаляет последний элемент


# dict_ = {1: 'Pizza', 2: 'Burger', 3: 'Steak'}
# remove = dict_.pop(2)
# print(dict_)
# dict_ = {1: 'Pizza', 2: 'Burger', 3: 'Steak'}
# remove2 = dict_.popitem()
# print(dict_)


roles = {
    1: 'Admin',
    2: 'Customer',
    3: 'Vendor'
}

users = {
    55:{
        'id': 55, 'role': roles[3], 'userName': 'Tirion'
    },
    
    12:{
        'id': 12, 'role': roles[1], 'userName': 'John Snow'
    },
    4:{
        'id': 4, 'role': roles[2], 'userName': 'Raychel'
    },
}
print(users)

product = {
    'id': 1,
    'title': 'Samsung Galaxy s23 Ultra',
    'description': 'Lorem ipsum',
    'price': 10000
}
print(product)



id_user = int(input('Vvedite id: '))
if users[id_user]['role'] == roles[1]:
    product['description'] = input('Vvedite opisaniye: ')
else:
    print('You don\'t have permissions!')

print(product)

