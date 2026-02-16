import requests
import json
from bs4 import BeautifulSoup
url = "https://google.com"

response = requests.get(url)
# j = response.json()
# print(j['origin'])

# print(type(j))
# print(json.dumps(j, indent=4, sort_keys=True)) # print json in pretty mode

soup = BeautifulSoup(response.content, 'lxml')
print(soup)

tag = soup.button
# print(tag.attrs)