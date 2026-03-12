import pytest
import json
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from Login_Page import LoginPage

#Python handling: Json
# test_data_path="../Data/test_Framework1.json"
# Get current file directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Join path properly
test_data_path = os.path.join(current_dir, "..", "Data", "test_Framework1.json")

with open(test_data_path) as json_file:
    test_data = json.load(json_file)   #load whole json
    test_list = test_data["data"]      #test_list store list of dictionary ,"data" is a key of json dictionary

@pytest.mark.smoke
@pytest.mark.parametrize("dataa", test_list)
def test_e2eProject(browserInfo, dataa):
    driver=browserInfo
    # driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    # driver.get("https://rahulshettyacademy.com/angularpractice/")
    # driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    loginpage =LoginPage(driver)
    print(loginpage.get_title())
    shop = loginpage.login(dataa["username"],dataa["password"])
    print(shop.get_title())
    shop.add_to_cart(dataa["product"])             #'Blackberry'
    Checkout = shop.go_to_cart()
    Checkout.checkout()
    Checkout.address()
    Checkout.validate_order()
    # driver.find_element(By.ID, "username").send_keys("rahulshettyacademy")
    # driver.find_element(By.ID, "password").send_keys("Learning@830$3mK2")
    # driver.find_element(By.CSS_SELECTOR, "input[value='admin']").click()
    # select = Select(driver.find_element(By.CSS_SELECTOR, "select[class='form-control']"))
    # select.select_by_visible_text("Teacher")
    # driver.find_element(By.ID, "terms").click()
    # driver.find_element(By.ID, "signInBtn").click()

    # driver.find_element(By.CSS_SELECTOR, "a[href*='/shop']").click()  # Regular expression "a[contain(href='shop')]"
    # items = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    # for item in items:
    #     if item.find_element(By.XPATH, "div/h4/a").text == "Blackberry":
    #         item.find_element(By.XPATH, "div/button").click()
    #         print(item.text)
    # driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
    # driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
    # driver.find_element(By.ID, "country").send_keys('ind')
    # wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='India']")))
    # driver.find_element(By.XPATH, "//a[text()='India']").click()
    # driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    # driver.find_element(By.CSS_SELECTOR, "input[value='Purchase']").click()  # "input[type='submit']"
    # Success = driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text
    # print(Success)
    # assert 'Success! Thank you!' in Success