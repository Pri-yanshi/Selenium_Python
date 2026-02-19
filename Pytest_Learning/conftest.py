import pytest


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