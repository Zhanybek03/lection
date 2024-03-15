from models import Product, Category


def get_all_categories():

    return Category.select(Category.id, Category.title)



def get_all_products():
    return Product.select()


categories = get_all_categories()
# print(categories)
print('Все категории в БД: ')
for category in categories:
    print(f'ID: {category} Title: {category.title}')
    print(category.title) #id

print()
products = get_all_products()
print(products)
print('Все продукты в БД: ')
for x in products:
    print(x)
    print(f'ID: {x.id}, Title: {x.title}, Price: {x.price}, Category: {x.category.title}')
