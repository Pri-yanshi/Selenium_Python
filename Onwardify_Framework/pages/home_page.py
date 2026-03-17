from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self,driver):
        self.driver = driver

    def open_website(self):
        self.driver.get("https://onwardify.com/")

    def get_title(self):
        return self.driver.title
    def get_url(self):
        return self.driver.current_url
    def console_log(self):
        return self.driver.get_log("browser")
    def navigate(self):
        self.driver.find_element(By.XPATH,"//li[@id='menu-item-2226']//a").click()
        self.driver.find_element(By.XPATH,"//li[@id='menu-item-2899']//a").click()
