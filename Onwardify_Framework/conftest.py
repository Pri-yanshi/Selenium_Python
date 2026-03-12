import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def Browser_info(request):
    chrome_options= Options()
    chrome_options.add_experimental_option("detach",True)
    chrome_options.set_capability("goog:loggingPrefs", {"browser": "ALL"})
    driver=webdriver.Chrome(options=chrome_options)

    yield driver
