from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from user_data import *
import json

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://ok.ru')
# user = driver.find_element(By.ID, 'field_email')
# user.send_keys(email)
# pwd = driver.find_element(By.ID, 'field_password')
# pwd.send_keys(password)
# sleep(1)
# pwd.send_keys(Keys.ENTER)
# sleep(5)

# with open("ok_cookie", 'w') as f:
#     json.dump(driver.get_cookies(), f)
with open("ok_cookie") as f:
    cookies = json.load(f)

for cook in cookies:
    driver.add_cookie(cook)

driver.refresh()
sleep(5)