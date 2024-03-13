# text = 'The more you learn, the more you earn.'
# leng() - возврощает длину текста считая каждый его символ
# len_text = len(text)
# print(text, len_text)
# print(text[:: -1])

# count_e = 0
# i = 0
# while i < len_text:
#     symbol = text[i]
#     if symbol == 'e' or symbol == 'E':
#         count_e += 1
#     print(symbol)
#     i += 1

# print(f'Symbol E is found: {count_e} times!')


# text = 'The more you learn, the more you earn.'
# # leng() - возврощает длину текста считая каждый его символ
# len_text = len(text)
# count_e = 0
# i = 0
# c = 0
# while text[i:]:
#     c += 1
#     i += 1
#     print(c)

# print(f'Symbol E is found: {count_e} times!')




# -------------------------------------------------

# Методы строк - dir()

# print(dir('hell'))

# count(value, [start]) - считает количество вхождений value в нашу строку

# text = 'hello o o o o o  hello '
# print(text.count('o'))
# print(text.count('l'))

# replace(old, new, [count]) - меняет в строке old символ на new, заменит count раз если число
# text = 'ha ha ha ha ha'
# res = text.replace('ha', 'ah')
# print(f'orginal:  {text}')
# print(f'result after replace: {res}')


# strip() - убирает пробельные символы в начале и в конце строки
# rstrip, lstrip
# a = '   hello   '
# print(len(a))
# res = a.strip()
# print(res, len(res), sep= '->')
# print(a.lstrip(), '1')
# print(a.rstrip(), '2')


# isdigit - проверяют 
# isnumeric - состоит ли наша строка
# isdecimal - из чисел

# num = input('enter a digit: ')
# print(f'Vvedino li chislo?: {num.isdigit()}')


# isalhpa - состоит ли наша строка из символов алфавита
# txt = 'Hello world'
# print(txt.isalpha())
# res = txt.replace(' ', '')
# print(res, res.isalpha())

# num = input('enter a digit: ')
# if num.isdigit:
#     num = int(num)
#     print((f'{num} * 5 = {num * 5}'))
# else:
#     print('you entered a non digit')

# split(separator) - разделяет строку на несколько частей по разделителю все части сохраняются в типе list 

# text = 'Let me speak in English'
# res = text.split('t')
# print(res)

# a = '#hello#life#love#Bishkek#'
# print(a[1:].split('#'))



# 'connector'.join(list) - соеденяет по connector строки которые были в list
ls = ['Anvar', 'John', "Jamie", "Osmon"]
print(ls)
res = ''.join(ls)
print(res)



# swapcase() - переводит все символы в противоположенный регистр
 
#  upper() = переводит все в верхний регистр 
# lower () = переводит все в верхний регистр

# text = 'Hello  HELLO OWN , фт and you my ittle borther'
# print(text.swapcase())
 
# index(value) - выводит индекс значения value внутри строки
# find(value) - делает тоже самое что и index, но если не нашел value то вернется -1



# text = 'Hello John Snow'
# print(text.find('a'))
# print(text.find('John'))
