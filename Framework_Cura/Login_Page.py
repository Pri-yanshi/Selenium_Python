from selenium.webdriver.common.by import By

from Appointment_Page import AppointmentPage


class LoginP:
    def __init__(self,Driver):
        self.driver = Driver
        self.user = By.ID, "txt-username"
        self.password = By.ID, "txt-password"
        self.log_btn = By.ID, "btn-login"

    def login(self,user, password):
        self.driver.find_element(*self.user).send_keys(user)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.log_btn).click()
        appoint =AppointmentPage(self.driver)
        return appoint