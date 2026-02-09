from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://vinothqaacademy.com/alert-and-popup/')
# driver.find_element(By.NAME, 'alertbox').click()
# sleep(2)
# alert_obj = driver.switch_to.alert
# print(alert_obj.text)
# alert_obj.accept()
# sleep(3)

# driver.find_element(By.NAME, 'confirmalertbox').click()
# conf_obj = driver.switch_to.alert
# print(conf_obj.text)
# sleep(1)
# # conf_obj.accept()
# conf_obj.dismiss()
# sleep(3)

driver.find_element(By.NAME, 'promptalertbox1234').click()
prompt_obj = driver.switch_to.alert
print(prompt_obj.text)
prompt_obj.send_keys("Yes")
sleep(2)
prompt_obj.accept()
# prompt_obj.dismiss()
answer = driver.find_element(By.ID, 'demoone')
print(answer.text)
sleep(3)