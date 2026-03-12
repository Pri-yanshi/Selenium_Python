import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store",default="chrome",help='browser selection')

@pytest.fixture(scope="function")
def browserInfo(request):   #request is default fixture which is available for whole framework
    options_chrome = Options()
    options_chrome.add_experimental_option("detach", True)
    browser_name= request.config.getoption("browser_name")  #configuration option is '--browser_name' in terminal use any browser
    if browser_name == "chrome":
        driver = webdriver.Chrome(options=options_chrome)
        driver.implicitly_wait(5)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(options=options_chrome)
        driver.implicitly_wait(5)
    # driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()
    yield driver  #before test function execution
    driver.close()  #post test function execution