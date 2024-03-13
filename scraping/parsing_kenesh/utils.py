from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

url = "https://kenesh.kg/deputies/"

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--disable-javascript")

# service = Service('path')
def get_deps_html_selenium(url):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    WebDriverWait(driver, 10).until((
        EC.presence_of_element_located((By.CLASS_NAME, 'card-title'))
    ))
    html = driver.page_source
    driver.quit() 
    return html



def get_html_selenium(url):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    element = WebDriverWait(driver, 10).until((
        EC.presence_of_element_located((By.CLASS_NAME, 'stretched-link'))
    ))

    sleep(10)
    
    html = driver.page_source
    driver.quit() 
    return html


def get_page_html_selenium(url):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    element = WebDriverWait(driver, 10).until((
        EC.presence_of_element_located((By.CLASS_NAME, 'section-footer'))
    ))
    page_btn = driver.find_elements(By.CSS_SELECTOR, '.page-item')
    i = 1
    res = {}
    while i <= 8:
        sleep(1.5)

        html = driver.page_source
        res[i] = (html)
        if i == 8:
            break
      
        element = page_btn[-1]
        if page_btn:
            ActionChains(driver).move_to_element(element).perform()
            sleep(0.5)
            element.click()
        i += 1
    # print([x.text for x in page_btn])
    
    driver.quit() 
    return res


# res = get_page_html_selenium('https://kenesh.kg/deputies')
# print(res)