from bs4 import BeautifulSoup
import requests
import json

url =  'https://www.walmart.com/ip/Samsung-32-Smart-Monitor-M5-M50D-FHD-with-Streaming-TV-and-Speakers-LS32DM50DENXGO/15669562011?classType=REGULAR&adsRedirect=true'

headers ={
    'Accept': "*/*",
    'Accept-encoding' : "gzip, deflate, br, zstd",
    'Accept-language': "en-US,en;q=0.9,it-IT;q=0.8,it;q=0.7",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

next_data = soup.find('script', id='__NEXT_DATA__')
# title = soup.find('h1', class_= 'lh-copy dark-gray mv1 f4 mh0 b')

data = json.loads(next_data.string)
initial_data = data['props']['pageProps']['initialData']['data']
product_data = initial_data['product']
reviews_data = initial_data.get('reviews', {}) # If reviews are not present, it will return an empty dictionary
price_data = product_data['priceInfo']



product_data_info = {
    'title': product_data['name'],
    'prv_price': product_data['priceInfo']['wasPrice']['price'],
    'current_price': product_data['priceInfo']['currentPrice']['price'],
    'short_description': product_data.get('shortDescription', 'No description available'),
    'rating': product_data.get('customerRating', {}).get('averageRating', 'No rating available'),
    'reviews_count': reviews_data.get('totalReviews', 0),
    'product_availability': product_data['availabilityStatus']

}
for key, value in product_data_info.items():
    print(f"{key.title()}: {value}")

# print(data['props']['pageProps']['initialData']['data']['product'].keys())

# print(data['props']['pageProps']['initialData']['data']['product']['primaryProductId'])
# print(data['props']['pageProps']['initialData']['data']['product']['shortDescription'])
# print(data['props']['pageProps']['initialData']['data']['product']['name'])
# print(data['props']['pageProps']['initialData']['data']['product']['priceInfo'].keys())




































# print(f"Price: {data['props']['pageProps']['initialData']['data']['product']['priceInfo']['currentPrice']['price']}")


# response = requests.get(url)

# soup = BeautifulSoup(response.text, 'html.parser')
# price = soup.find('span', itemprop='price')
# for p in price:
#     px = p.text.strip().split('Now')[-1]
#     print(px)