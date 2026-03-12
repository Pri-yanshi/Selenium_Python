import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Framework_Cura.conftest import browserDetail
from Login_Page import LoginP


def test_Cura(browserDetail):
    driver = browserDetail
    wait = WebDriverWait(driver,10)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    driver.find_element(By.ID,"btn-make-appointment").click()

    wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"form-group")))
    loginpage = LoginP(driver)
    appointm = loginpage.login("John Doe","ThisIsNotAPassword")
    appointm.appointment()

