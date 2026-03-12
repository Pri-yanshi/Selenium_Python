from selenium.webdriver.common.by import By

from Checkout_Page import Checkout_Confirmation
from Utils.browser_util import BrowserUtils


class ShopPage(BrowserUtils):
    def __init__(self, Driver):
        super().__init__(Driver)
        self.driver = Driver
        self.shop = By.CSS_SELECTOR, "a[href*='/shop']"
        self.items = By.XPATH, "//div[@class='card h-100']"
        self.product = By.XPATH, "div/h4/a"
        self.add = By.XPATH, "div/button"
        self.cart = By.CSS_SELECTOR, "a[class*='btn-primary']"



    def add_to_cart(self, productname):
        self.driver.find_element(*self.shop).click()  # Regular expression "a[contain(href='shop')]"
        items = self.driver.find_elements(*self.items)
        for item in items:
            if item.find_element(*self.product).text == productname:   #"Blackberry"
                item.find_element(*self.add).click()
                print(item.text)

    def go_to_cart(self):
        self.driver.find_element(*self.cart).click()
        checkout_conf = Checkout_Confirmation(self.driver)
        return checkout_conf