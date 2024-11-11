import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://mystat.itstep.org/homework'
response = requests.get(url)

if response.status_code == 200:
    print("HTML-код сторінки отримано успішно.")
else:
    print(f"Помилка при виконанні запиту: {response.status_code}")
    exit()

