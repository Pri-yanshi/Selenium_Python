import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# driver=webdriver.Chrome()
# driver.get("https://www.saucedemo.com/")
# driver.maximize_window()
# time.sleep(3)
# # username= driver.find_element(By.ID,"user-name")
# # password = driver.find_element(By.ID,"password")
# username= driver.find_element(By.XPATH,"//input[@name='user-name']")
# password = driver.find_element(By.XPATH,"//input[@name='password']")
# username.send_keys("standard_user")
# password.send_keys("secret_sauce")
# driver.find_element(By.XPATH,"//input[@name='login-button']").click()
# time.sleep(5)
# # Using Contains() for partial match(if id, class changes dynamically use contains)
# # Script relative//tagname[contains(@attribute,'PartialText')]
# addToCart=driver.find_element(By.XPATH,"//button[contains(@id,'sauce-labs-backpack')]")
# addToCart.click()
# driver.find_element(By.XPATH,"//div[text()='Sauce Labs Fleece Jacket']").click()
#
# time.sleep(5)
driver=webdriver.Chrome()
driver.get("https://tms.gtrtek.com/")
driver.maximize_window()
time.sleep(5)
username= driver.find_element(By.XPATH,"//input[@name='loginfmt']")
username.send_keys("priyanshi.maurya@Gtrtek.com")
driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(4)
password = driver.find_element(By.XPATH,"//input[@name='passwd']")
password.send_keys("")
time.sleep(4)