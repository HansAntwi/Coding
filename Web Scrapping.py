import requests
from bs4 import BeautifulSoup

url = 'https://www.scrapethissite.com/pages/forms/'

request = requests.get(url)

soup = BeautifulSoup(request.text, 'html.parser')

# print(soup.prettify)

table = soup.find_all('tr')
print(table)