from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
# driver.set_window_size
driver.get("https://web.whatsapp.com")
input("Press Enter after scanning QR code")
sleep(3)
driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div/div[4]/header/header/div/span/div/div[1]/span/button/div/div/div[1]/span').click()
search = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div/div[3]/div[1]/div/span/div/span/div/div[1]/div[2]/div/div/div[1]/p')
search.click()
search.send_keys('545773947')
search.send_keys(Keys.ENTER)
sleep(1)
message = driver.switch_to.active_element
message.send_keys("Hello, friend")
message.send_keys(Keys.ENTER)
sleep(5)