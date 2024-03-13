# JSON - JavaSript Object Notation
# Единный текстовый формат данных, был создан для хранения и передачи данных между сервисами, проектами.
# <filename>.json файл в формате JSON
# {
#     "id": 1,
#     "autor": {
#         "name": "Ed Sheeran"
#         "age": 35,

#     },
#     't'
# }

# js object == {key: value}
# Py dict == {key: value}
# JSON == {key: value}

# Процессы Сериализации и Десериализации данных (конвертация)

# Сериализации (запис данных в JSON) - это перевод из  Python  в JSON формат
# dump - записывает данные в файл формата JSON
# dumps - записывает данные в текст формата JSON

# Десериализации (чтение данных из JSON) - это поцесс перевода из JSON в PY dict


# load - функция которая считывает данные из файла JSON
# loads - функция которая считывает данные из текста JSON


# import json 
# dict_ = {
#     'name': 'John Snow',
#     'age': 24,
#     'status': True,
#     'wife': False,
#     'children': None
# }
# print(dict_,type(dict_))


# json_text = json.dumps(dict_)
# print()
# print(json_text, type(json_text))



# import json 
# dict_ = {
#     'name': 'John Snow',
#     'age': 24,
#     'status': True,
#     'wife': False,
#     'children': None
# }
# print(dict_,type(dict_)) 


# with open('new.json', 'w') as file:
#     json.dump(dict_, file, indent=4)
# --------------------

# процес Десериализации
# import json
# with open('new.json', 'r') as file:
#     json_data = file.read()

# print(json_data, type(json_data))
# dict_ = json.loads(json_data)
# print()
# print(dict_, type(dict_))


# import json
# with open('new.json', 'r') as file:

#     dict_ = json.load(file)

# print(dict_, type(dict_))
 