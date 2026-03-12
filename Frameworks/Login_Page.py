from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Shop_Page import ShopPage
from Utils.browser_util import BrowserUtils


class LoginPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username = By.ID, "username"
        self.password = By.ID, "password"
        self.admin = By.CSS_SELECTOR, "input[value='admin']"
        self.selectt = By.CSS_SELECTOR, "select[class='form-control']"
        self.terms = By.ID, "terms"
        self.sign = By.ID, "signInBtn"


    def login(self,username,password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.admin).click()
        select = Select(self.driver.find_element(*self.selectt))
        select.select_by_visible_text("Teacher")
        self.driver.find_element(*self.terms).click()
        self.driver.find_element(*self.sign).click()
        shoppage = ShopPage(self.driver)
        return shoppage