
a = [1, 1, 2.3, 3, -5, 8, -13, -21, 34.5, 55, 89]

b = [1, 2.3, 3, 4, -5, 6, 7, 8, 9, -10, 11, -12, -13, 34.5]

res = []
negative_list = []
for i in b:
    if i in a:
        res.append(i)

for i in res:
    if i < 0:
        delete = res.pop(res.index(i))
        negative_list.append(abs(delete))

print(res)
print(pow(res[0], 3), pow(res[-1],3))



 

Banknote = ['Абдылас Малдыбаев', 'Бубусара Бейшеналиева', 'Касым Тыныстанов', 'Тоголок Молдо', 'Курманджан Датка',  'Бенджамин Франклин']



Banknote[-1] = 'Токтогула Сатылганова'



Banknote.append('Алыкул Осмонов')
Banknote.append('Саякбай Каралаев')
Banknote.append('Жусуп Баласагын')


b = int(input('Vvedite naminal banknota: '))
if b == 200:
    print('Алыкул Осмонов')
elif b == 500:
    print('Саякбай Каралаев')
elif b == 1000:
    print('Жусуп Баласагын')
elif b == 100:
    print('Токтогул Сатылганов')
elif b == 1:
    print('Абдылас Малдыбаев')
elif b == 50:
    print(Banknote[4])
elif b == 5:
    print(Banknote[1])
elif b == 10:
    print(Banknote[0])
else:
    print('Error!')





user_1 = int(input('Enter a day of week: '))
user_2 = int(input('Enter hours that you worked today: '))
if user_1 == 1:
    print('Today is monday')
    print(f'tebe ostalos rabotat {8 - user_2}')
elif user_1 == 2:
    print('Today is tuesday')
    print(f'Тебе осталось работать {8 - user_2}')

elif user_1 == 3:
    print('Today is Wednesday')
    print(f'Тебе осталось работать {8 - user_2}')

elif user_1 == 4:
    print('Today is Thursday')
    print(f'Тебе осталось работать {8 - user_2}')

elif user_1 == 5:
    print('Today is Friday')
    if user_2 < 2:
        print('Можешь уходить!!')
    else:
        print(f'Тебе осталось работать{8 - user_2}')


elif user_1 == 6:
    print('Today is Saturday')
    print(f'Тебе осталось работать {8 - user_2}')

elif user_1 == 7:
    print('Today is Sunday')
    print(f'Тебе осталось работать {8 - user_2}')



rating = int(input('Что получил по математике? '))

if rating <= 2 or rating <= 3:
   print('Плохо. Марш учиться!')
elif rating == 4 or rating == 5:
   print('Молодец! Можешь отдохнуть.')
   



ls = [1, '2', 3, 4, '5', "шесть", "семь"]
ls1 = []
ch = []
nech = []

for i in ls:
    if i == 'шесть':
        ls1.append(6)
    elif i == 'семь':
        ls1.append(7)
    else:
        ls1.append(int(i))

print(sum(ls1))

for i in ls1:
    if i % 2 == 0:
        ch.append(i)
    else:
        nech.append(i)



