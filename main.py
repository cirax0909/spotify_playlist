import requests
from bs4 import BeautifulSoup

time = input('what year you would like to travel to in YYYY-MM-DD format?')

response = requests.get("https://www.billboard.com/charts/hot-100/2000-08-12/")
web = response.text

soup = BeautifulSoup(web, 'html.parser')
print(soup)