from bs4 import BeautifulSoup
import requests
import csv
import pprint



def parsing_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser') #lxml the most fast stuff
    # print(soup)
    countainer = soup.find('div', class_='table-view-list')
    cars = countainer.find_all('div', class_='list-item')
    result = []
    for car in cars:
        name = car.find('h2', class_='name').text.strip()
        # print(name)
        try:
            img = car.find('img', class_='lazy-image-attr').get('src')
        except Exception as e:
            img = f'No image, {e}!'
        # print(img)
        # print()
        price = car.find('div', class_='block price').find('strong').text.srip()
        # print(price)
        desc =' '.join(car.find('div', class_="item-info-wrapper").text.split())
        # print(desc)
        # print()
        data = {'title': name, 'desc': desc, 'price': price, 'img': img}
        result.append(data)

    return result


    # print(type(response.text))
# pprint.pprint(parsing_data(url))
def get_last_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    pages = soup.find_all('a', class_="page-link")[-1]
    return int(pages.get('data-page'))

def prepare_csv():
    with open('cars.csv', 'w') as file:
        fieldnames = ['w', 'name', 'desc', 'price', 'img']
        writer =csv.DictWriter(file, fieldnames)
        writer.writerow({
            'w': '№',
            'name': 'Name:',
            'desc': 'Description:',
            'price': 'Price:',
            'img': 'Image Url:'
        })
def write_to_scv(data: list):
    with open('cars.csv', 'a') as file:
        global count
        fieldnames = ['№', 'name', 'desc', 'price', 'img']
        writer =csv.DictWriter(file, fieldnames)
        for car in data:
            writer.writerow({
                '№': count,
                'name': car['title'],
                'desc': car['desc'],
                'price': car['price'],
                'img': car['img'],
            })
            count += 1




url = f'https://www.mashina.kg/search/all/'
last_page = (get_last_page(url))

prepare_csv()
count = 1
i = 1
while i <= last_page:
    page_url = f'https://www.mashina.kg/search/all/?page={i}'
    data = parsing_data(page_url)
    
    write_to_scv(data)
    print(f'Спарсили {i}/{last_page} страницу!')
    
    i += 1
# data = parsing_data(url)
# write_to_scv(data)
# SELENIUM -parsing