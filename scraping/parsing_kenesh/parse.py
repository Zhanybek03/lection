import csv
from bs4 import BeautifulSoup
from datetime import datetime
from utils import get_page_html_selenium, get_deps_html_selenium
from multiprocessing import Pool



base_url = 'https://kenesh.kg'
deputs_url = base_url + '/deputies/'


def get_soup(html):
    soup = BeautifulSoup(html, 'lxml')
    return soup

def get_personal_link(soup):
    container = soup.find('div', class_='section-body')
    items = container.find_all('div', class_='card')[:12]
    links = [
        base_url + x.find('a').get('href')
             for x in items
    ]
    return links

def get_all_page_links(pages):
    res = []
    for i in range(1, 9):
        html = pages[i]
        soup = get_soup(html)
        url = get_personal_link(soup)
        res.extend(url)
    return res

def get_deps_data(link):
    html = get_deps_html_selenium(link)
    soup = get_soup(html)
    name =soup.find('h5', class_='card-title').text
    info_divs = soup.find_all('div', class_='card-subtitle')
    info = ' '.join(x.text for x in info_divs)
    bio = soup.find('article', class_='clearfix').text.strip().replace('Powered by Froala Editor', '')
    img = soup.find('img', class_='card-img-top').get('src').replace(' ', '%20')
    write_to_csv(name, info, bio, img, link)

def prepare_csv():
    with open('deputy.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['FIO:', 'Info:', 'Bio:', 'Image:', 'Link to page:'])

def write_to_csv(name, info, bio, img, url):
    with open('deputy.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([name, info, bio, img, url])
        print(f'{name} - parsed!')


# all_pages = get_page_html_selenium(deputs_url)
# links = get_all_page_links(all_pages)
# print(links, len(links))
# prepare_csv()
# get_deps_data('https://kenesh.kg/ru/deputies/426')

def main():
    prepare_csv()
    print('Parsing links...')
    all_pages = get_page_html_selenium(deputs_url)
    links = get_all_page_links(all_pages)

    # for link in links: #последовательно
    #     get_deps_data(link)
    #паралельно (мультипроцессы)
    with Pool(8) as pool:
        pool.map(get_deps_data, links)


if __name__ == '__main__':
    start = datetime.now()
    main()
    finish = datetime.now()
    print(f'Parsing takes: {finish - start} time!')
    
# Пагинация - карусель
#13:48
# 07:00