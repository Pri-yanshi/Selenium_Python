from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.implicitly_wait(10)
parent = driver.current_window_handle
driver.find_element(By.CSS_SELECTOR,".blinkingText").click()
wait.until(EC.number_of_windows_to_be(2))

for window in driver.window_handles:
    if window != parent:
       driver.switch_to.window(window)

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".im-para.red")))
text_element = driver.find_element(By.CSS_SELECTOR,".im-para.red").text
print(text_element)
username_value = text_element.split()[4]
print(username_value)
driver.switch_to.window(parent)
driver.find_element(By.ID,"username").send_keys(username_value)
driver.find_element(By.ID,"password").send_keys("Learning@830$3mK2")
driver.find_element(By.CSS_SELECTOR,"input[value='admin']").click()
select=Select(driver.find_element(By.CSS_SELECTOR,"select[class='form-control']"))
select.select_by_visible_text("Teacher")
driver.find_element(By.ID,"terms").click()
driver.find_element(By.ID,"signInBtn").click()
error_msg = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".alert.alert-danger.col-md-12"))).text
print(error_msg)

