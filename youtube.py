from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://www.youtube.com/watch?v=voO12-fh-eU")
#driver.execute_script("window.scrollBy(0, 500)")
sleep(3)
body = driver.find_element(By.TAG_NAME, 'body')
while True:
    try:
        body.send_keys(Keys.ARROW_DOWN)
        if driver.find_element(By.XPATH, '//*[@id="count"]/yt-formatted-string/span[1]'):
            comment = driver.find_element(By.XPATH, '//*[@id="count"]/yt-formatted-string/span[1]')
            print(f"There are {comment.text} comments for this video")
            break
    except Exception:
        pass





# driver.execute_script("window.open('https://google.com', '_blank')")
# sleep(2)
# driver.switch_to.window(driver.window_handles[1])
# search = driver.find_element(By.ID, 'APjFqb')
# search.click()
# search.send_keys("selenium")
# search.send_keys(Keys.ENTER)
# sleep(3)
# driver.execute_script("window.open('https://cnn.com', '_blank')")
# sleep(3)
# for window in driver.window_handles:
#     driver.switch_to.window(window)
#     sleep(2)