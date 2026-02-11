from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
#----------------------radio button------------------------------------------------
wait = WebDriverWait(driver, 20)
radioB = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@value='male' and @name='gender']")))
radioB.click()
assert radioB.is_selected(),"Male radio button not selected"

#-----------------------------------Static Dropdown---------------------------------------------

dropdown=driver.find_element(By.ID,"country")
select=Select(dropdown)
select.select_by_value("uk")
selected_option=select.first_selected_option.text
assert selected_option == 'Germany',"Germany is not selected"

#------------------------------------Dynamic Dropdown------------------------------------------------------
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
assert 'Poland' in driver.current_url
