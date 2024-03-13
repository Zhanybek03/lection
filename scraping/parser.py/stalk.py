from selenium  import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
# from webdriver_manager.chrome import ChromeDriverManager
import time
import csv
import requests

def parsing_data(url):
   
    chrome_driver = '/usr/bin/chromedriver'
    service = Service(executable_path=chrome_driver)
    options = webdriver.ChromeOptions()
    # options.headless = False
    browser = webdriver.Chrome(service=service, options=options)
    url = 'https://global.wildberries.ru/catalog?category=9492'
    browser.get(url)
    time.sleep(5)
    html = browser.page_source
    result = []
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)
    container = soup.find('div', class_='card-grid')
    nouts = soup.find_all('div', class_='card-cell')
    for nout in nouts:
        title = nout.find('div', class_="b-card__info-row").text.strip()
        price = nout.find('div', class_="b-card__price").text.strip()
        image = nout.find('img', class_="main-img").get('src')
        data = {'title': title, 'price': price, 'image': image}
        result.append(data)
    return result


def prepare_csv():
    with open('willbers.csv', 'w') as file:
        fieldnames = ['№', 'title', 'price', 'image']
        writer =csv.DictWriter(file, fieldnames)
        writer.writerow( {
            '№': '№',
            'title': 'title', 
            'price': 'price', 
            'image': 'image'})
        
count = 1
def write_to_scv(data):
    with open('willbers.csv', 'a') as file:
        global count
        fieldnames = ['№', 'title', 'price', 'image']
        writer =csv.DictWriter(file, fieldnames)
        for willbers in data:
            writer.writerow({
                '№': count,
                'title': willbers['title'],
                'price': willbers['price'],
                'image': willbers['image'],
            })
            count += 1


url = f'https://global.wildberries.ru/catalog?category=9492'

prepare_csv()
count = 1
i = 1
while i <= 28:
    page_url = f'https://global.wildberries.ru/catalog?category=9492page={i}'

    data = parsing_data(page_url)
    write_to_scv(data)
    print(f'Спарсили {i}/{28} страницу!')
    
    i += 1
# prepare_csv()
# write_to_scv(result)