from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/upload')
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH,value="//input[@id='file-upload']").send_keys("C:\\Users\\priyanshi\\OneDrive\\Pictures\\bear.png")
time.sleep(1)
driver.find_element(By.XPATH,value="//input[@id='file-submit']").click()
time.sleep(5)
driver.quit()
