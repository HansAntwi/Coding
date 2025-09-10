import requests
from bs4 import BeautifulSoup

headers = {
    "Accept": "*/*",
    "Accept-encoding": "gzip, deflate, br, zstd",
    "Accept-language": "en-US,en;q=0.9,it-IT;q=0.8,it;q=0.7",
    "Content-Type": "text/plain;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
}
# matchweek = range(1,39)
# for i in matchweek:
#     print(f'Processing matchweek {i}')

url = 'https://www.premierleague.com/en/tables?competition=8&season=2025&round=L_1&matchweek=1&ha=-1'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

league_table = soup.find_all('th')
print(league_table)
# for table in league_table:
#     print(table.text.strip())

# for i, table in enumerate(league_table):
#     print(f'{i}: {table.text.strip()}\n')
