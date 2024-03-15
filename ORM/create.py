import peewee
from models import Category, Product
import random

def add_category(name):
    try:
        obj = Category(title=name.lower().strip())
        obj.save()
        print(f'Сохранили катергорию {obj} - {obj.title}')

    except (peewee.IntegrityError, peewee.InternalError):
        print(f'{name.lower().strip()} - это категория уже существует!')


# add_category('Laptop')
# add_category('    PC    ')
# add_category('Sony Playstations')
# add_category('Tables')
# add_category('erarphones')
# add_category('Smartphones')


def add_product(name, price, category_name):
    category_name = category_name.lower().strip()
    try:
        category = Category.get(title=category_name)
        print(category, category.title, category.created_at," !!!")
    except peewee.DoesNotExist:
        print(f'Категории {category_name} не существует!')
    else: 
        obj = Product(title=name, price=price, category_id=category)
        obj.save()
        print(f'Сохранили товар {obj} - {obj.title}')

add_product('Acer Swift', 1000, 'Laptop')
add_product('Iphone 14 Pro Max', 1200, 'Smartphones')
add_product('Samsung S22 ULTRA', 1000, 'Smartphones')
add_product('Airpods Pro', 500, 'earphones')
add_product('Macbook Air M1', 900, 'Laptop')
add_product('Toshiba ZT', 400, 'Laptop')
add_product('HP Envy 360', 800, 'Laptop')
