from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.XPATH,"//button[@id='openwindow']").click()
driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.XPATH,"//li[@class='nav-item']//a[normalize-space()='Courses']").click()
driver.switch_to.window(driver.window_handles[0])
