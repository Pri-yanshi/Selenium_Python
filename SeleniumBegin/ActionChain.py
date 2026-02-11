from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
action = ActionChains(driver)

# Hover on Button
action.move_to_element(driver.find_element(By.XPATH,"//button[@class='dropbtn']")).perform()
action.click_and_hold(driver.find_element(By.XPATH,"//a[contains(text(),'Mobile')]")).click().perform()
time.sleep(7)
#Double_Click, Context Click is used for Right click
action.double_click(driver.find_element(By.XPATH,"//input[@id='field1']")).perform()

time.sleep(7)