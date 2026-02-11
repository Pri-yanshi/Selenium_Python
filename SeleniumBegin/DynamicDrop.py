from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
#----------------------radio button------------------------------------------------
wait = WebDriverWait(driver, 20)


driver.find_element(By.ID,"Wikipedia1_wikipedia-search-input").send_keys('p')
driver.find_element(By.CLASS_NAME, "wikipedia-search-button").click()

results = wait.until(
    EC.visibility_of_all_elements_located(
        (By.XPATH, "//div[@id='wikipedia-search-result-link']//a")
    )
)

for result in results:
    if result.text == "Public Domain":
        result.click()
        break
#assert 'Public Domain' in driver.current_url