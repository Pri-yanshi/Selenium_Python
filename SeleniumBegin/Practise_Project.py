from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "a[href*='/shop']").click()  # Regular expression "a[contain(href='shop')]"
items= driver.find_elements(By.XPATH, "//div[@class='card h-100']")
for item in items:
    if item.find_element(By.XPATH,"div/h4/a").text == "Blackberry":
        item.find_element(By.XPATH,"div/button").click()
        print(item.text)
driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys('ind')
wait.until(EC.presence_of_element_located((By.XPATH,"//a[text()='India']")))
driver.find_element(By.XPATH,"//a[text()='India']").click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR,"input[value='Purchase']").click()    #"input[type='submit']"
Success= driver.find_element(By.CSS_SELECTOR,"div[class*='alert-success']").text
print(Success)
assert 'Success! Thank you!' in Success




