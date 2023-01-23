import requests
from bs4 import BeautifulSoup

url = 'https://horo.mail.ru/'
response = requests.get(url)
print(response.status_code)
soup = BeautifulSoup(response.text, 'lxml')

quotes = soup.find_all('a', class_='p-imaged-item')
resp_zn = []
print(quotes)


