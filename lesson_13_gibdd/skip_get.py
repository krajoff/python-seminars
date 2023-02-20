import random
import requests
from selenium.webdriver.common.by import By
from create_driver import driver


def first_page_skip():
    url = 'https://xn--90adear.xn--p1ai/request_main'
    driver.get(url)
    driver.find_element(By.CLASS_NAME, 'checkbox').click()
    driver.find_element(By.CLASS_NAME, 'u-form__sbt').click()


def get_captcha():
    img = driver.find_element(By.XPATH, "//img[@class='captcha-img']")
    src = img.get_attribute('src')
    img = requests.get(src)
    file_name = 'captcha' + str(random.randint(0, 10000000)) + '.jpg'
    file_path = 'captcha/' + file_name
    with open(file_path, 'wb') as f:
        f.write(img.content)
    return file_path
