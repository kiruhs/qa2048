from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.youtube.com/watch?v=voO12-fh-eU")
driver.execute_script("window.scrollBy(0, 300")
try:
    if driver.find_element(By.XPATH, '//*[@id="count"]/yt-formatted-string/span[1]'):
        comment = driver.find_element(By.XPATH, '//*[@id="count"]/yt-formatted-string/span[1]')
        print(f"There are {comment.text} comments for this video")
except Exception:
    pass