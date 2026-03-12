from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AppointmentPage:
    def __init__(self,Driver):
        self.driver = Driver
        self.facility = By.ID,"combo_facility"
        self.apply = By.ID,"chk_hospotal_readmission"
        self.program = By.ID,"radio_program_medicaid"

    def appointment(self):
        select = Select(self.driver.find_element(*self.facility))
        select.select_by_visible_text("Seoul CURA Healthcare Center")
        self.driver.find_element(*self.apply).click()
        self.driver.find_element(*self.program).click()
        self.driver.find_element(By.CSS_SELECTOR,"span[class*= 'glyphicon-calendar']").click()
        self.driver.find_element(By.CSS_SELECTOR,"div[class='datepicker-days'] th[class='datepicker-switch']").click()
        curr_month = self.driver.find_element(By.XPATH,"//span[@class='month focused']").text
        self.driver.find_element(By.CSS_SELECTOR, "div[class='datepicker-months']  th[class='datepicker-switch']").click()
        curr_year = self.driver.find_element(By.CSS_SELECTOR,"div[class='datepicker-years'] th[class='datepicker-switch']").text
        print(curr_month,curr_year)

        # while curr_year != '2029':
        #     self.driver.find_element(By.CSS_SELECTOR,"div[class='datepicker-months'] th[class='next']").click()
        #     curr_year = self.driver.find_element(By.CSS_SELECTOR,
        #                                          "div[class='datepicker-months'] th[class='datepicker-switch']").text
        # self.driver.find_element(By.XPATH,"//span[text()='Oct']").click()
        # self.driver.find_element(By.CSS_SELECTOR,"tbody tr:nth-child(4) td:nth-child(4)").click()

        while curr_year != '2040-2049':
            self.driver.find_element(By.CSS_SELECTOR,
                                                 "div[class='datepicker-years'] th[class='next']").click()
            curr_year = self.driver.find_element(By.CSS_SELECTOR,
                                                 "div[class='datepicker-years'] th[class='datepicker-switch']").text
        self.driver.find_element(By.XPATH,"//span[text()='2045']").click()
        self.driver.find_element(By.XPATH,"//span[text()='Oct']").click()
        self.driver.find_element(By.CSS_SELECTOR,"tbody tr:nth-child(4) td:nth-child(4)").click()

        self.driver.find_element(By.ID,"txt_comment").send_keys("Health Issue")
        self.driver.find_element(By.XPATH,"//button[@id = 'btn-book-appointment']").click()

