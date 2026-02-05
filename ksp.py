from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Chrome()
driver.maximize_window()
url = "https://ksp.co.il"
driver.get(url)
but = driver.find_element(By.XPATH, '//*[@id="site-header"]/div/div/div[2]/button')
but.click()
sleep(1)
first = driver.find_element(By.XPATH, '/html/body/main/div/div[3]/div[1]/div[2]/div/div/div[2]/div/ul[1]/li[1]/div[2]/span')
ActionChains(driver).move_to_element(first).perform()
sleep(1)
second = driver.find_element(By.XPATH, '/html/body/main/div/div[3]/div[1]/div[2]/div/div/div[2]/div/ul[2]/li[3]/div[2]/span')
ActionChains(driver).move_to_element(second).perform()
sleep(1)
driver.find_element(By.XPATH, '/html/body/main/div/div[3]/div[1]/div[2]/div/div/div[2]/div/ul[3]/li[1]/div[2]/span').click()
sleep(4)
page_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    driver.implicitly_wait(3)
    sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if page_height == new_height:
        break
    page_height = new_height

    try:
        link = driver.find_element(By.XPATH, "//a[contains(text(), '83LK009HIV')]")
        href = link.get_attribute("href")
        driver.get(href)
        print("The item found")
        break
    except NoSuchElementException:
        pass

sleep(5)