from pprint import pprint
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.globes.co.il/portal/instrument.aspx?instrumentId=60&mode=trades")
sleep(5)

deals = driver.find_element(By.XPATH, '//*[@id="divTrade"]/table[2]')
#soup = BeautifulSoup(deals.text, 'lxml')
# print(deals.text)

data = []
for row in deals.find_elements(By.TAG_NAME, 'tr'):
    cols = row.find_elements(By.TAG_NAME, 'td')
    data.append({f'column{c+1}': cols[c].text for c in range(len(cols))})

pprint(data)

titles = driver.find_element(By.XPATH, '//*[@id="tableTop"]')
data1 = []
row = titles.find_element(By.TAG_NAME, 'tr')
cols = row.find_elements(By.TAG_NAME, 'th')
data1.append({f'column{c+1}': cols[c].text for c in range(len(cols))})

driver.close()

for rows in data:
    data1.append(rows)

with open("globes.csv", 'w', newline='', encoding='utf8') as file:
    my_fields = [f'column{c+1}' for c in range(len(cols))]
    writer = csv.DictWriter(file, fieldnames=my_fields)
    writer.writerows(data1)

