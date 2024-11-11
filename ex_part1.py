import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://www.example.com'
response = requests.get(url)

if response.status_code == 200:
    print("HTML-код сторінки отримано успішно.")
else:
    print(f"Помилка при виконанні запиту: {response.status_code}")
    exit()

