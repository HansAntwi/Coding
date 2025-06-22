import requests
from bs4 import BeautifulSoup

url = 'https://www.scrapethissite.com/pages/forms/'

request = requests.get(url)

soup = BeautifulSoup(request.text, 'html.parser')

# print(soup.prettify)

table = soup.find_all('table')
# print(table)


# getting headers
headers = soup.find_all('th')
headers1 = [title.text.strip() for title in headers]

import pandas as pd
df = pd.DataFrame(columns=headers1)

# print(df)

# method 2
# table_headers = []
# for title in headers:
#     title = title.text.strip()
#     table_headers.append(title)
    
# print(table_headers)
# print(headers1)

rows = soup.find_all('tr')
all_rows = []
for row_data in rows[1:]:
    row_cell = row_data.find_all('td')
    rows_data = []
    
    for data in row_cell:
        data = data.text.strip()
        rows_data.append(data)
    # print(rows_data)
    
    if row_data:
        all_rows.append(rows_data)
    # print(rows_data)
        
df = pd.DataFrame(all_rows, columns=headers1)
print(df)


df.to_csv(r'C:\Users\HANS ANTWI\OneDrive\Documents\Python Coding\Coding\Hockey_Teams.csv', index = False)