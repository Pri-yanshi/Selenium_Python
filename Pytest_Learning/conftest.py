import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='class')   #this fixture scope for class and at last yield will be executing
def setup(): # it will invoke the browser
    print('It will run first')
    yield   # teardown ,it will close the browser and delete the cookies after testcase has executed
    print(' It will execute at last')
@pytest.fixture()
def dataload():
    print('user profile data is created')
    return ['Priyanshi','Maurya','priyanshi@gmail.com']

@pytest.fixture(params=[('Chrome','Priyanshi','Maurya'),('FireFox','Maurya'),('Linux','SS')])
def cross_browser(request):
    return request.param


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store",default="chrome",help='browser selection')

@pytest.fixture(scope='function',params=[('October',2025,23)])     # params should store list of tuple
def calendar(request):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    browser_name=request.config.getoption('browser_name')
    if browser_name == 'chrome':
        driver = webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(10)
    driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")
    yield driver,request.param
    driver.close()
