from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class Checkout_Confirmation:
    def __init__(self, driver):
        self.driver = driver
        self.check = By.XPATH, "//button[@class='btn btn-success']"
        self.country = By.ID, "country"
        self.country_name = By.XPATH, "//a[text()='India']"
        self.checkbox = By.XPATH, "//div[@class='checkbox checkbox-primary']"
        self.purchase = By.CSS_SELECTOR, "input[value='Purchase']"
        self.success = By.CSS_SELECTOR, "div[class*='alert-success']"


    def checkout(self):
        self.driver.find_element(*self.check).click()

    def address(self):
        self.driver.find_element(*self.country).send_keys('ind')
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((self.country_name)))
        self.driver.find_element(*self.country_name).click()
        self.driver.find_element(*self.checkbox).click()

    def validate_order(self):
        self.driver.find_element(*self.purchase).click()  # "input[type='submit']"
        Success = self.driver.find_element(*self.success).text
        print(Success)
        assert 'Success! Thank you!' in Success