import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



@pytest.fixture(scope="function")
def browserDetail(request):
    option_chrome = Options()
    option_chrome.add_experimental_option("detach",True)
    driver =  webdriver.Chrome(options=option_chrome)

    driver.implicitly_wait(10)
    yield driver
    # driver.close()



