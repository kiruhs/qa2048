import requests
import json
from bs4 import BeautifulSoup
from requests.exceptions import JSONDecodeError
import re
from pprint import pprint

# url = "https://google.com"

# response = requests.get(url)
# j = response.json()
# print(j['origin'])

# print(type(j))
# print(json.dumps(j, indent=4, sort_keys=True)) # print json in pretty mode

# soup = BeautifulSoup(response.content, 'lxml')
# print(soup)

# tag = soup.button
# print(tag.attrs)

response = requests.get('https://github.com')

# try:
#     print(response.json())
# except JSONDecodeError:
#     print("cannot extract JSON from requested server")
# finally:
#     text = response.text
# print(text)

soup = BeautifulSoup(response.content, 'lxml')
# print(soup)

# tag = soup.button
# print(tag.attrs)
# print(tag.attrs['class'][2])

# buttons = soup.find_all('button')
# print(len(buttons))
# for b in buttons:
#     print(b.attrs)

# print(buttons[-1])

# print(soup.a.get('href'))
# for link in range(len(soup.find_all('a'))):
#     if re.search('^http', soup.find_all('a')[link].get('href')):
#         print(link+1, ': ', soup.find_all('a')[link].get('href'))


# result = re.search('ell', "Helo, world, llo")
# print(result)

# h = soup.find_all('a', href=re.compile('http'))
# print(h)

# print(soup.find_all('title', string='American Airlines'))

# for tag in soup.find_all():
#     print(tag.name)

tag_list = [tag.name for tag in soup.find_all()]
# print(len(set(tag_list)))
tag_dict = {}
for i in tag_list:
    if i in tag_dict:
        tag_dict[i] += 1
    else:
        tag_dict[i] = 1

# print(tag_dict)
pprint(dict(sorted(tag_dict.items(), key=lambda tg: tg[1], reverse=True)), sort_dicts=False)