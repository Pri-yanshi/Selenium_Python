import pytest


@pytest.mark.smoke
@pytest.mark.skip  # it will skip test
def test_FirstPr():
    msg= 'Hello'
    assert msg == 'Hii','Test failed because string do not match'

def test_SecondTestCase():
    a=4
    b=3
    assert a+b==7,'test pass'

# @pytest.fixture()
# def setup(): # it will invoke the browser
#     print('It will run first')
#     yield   # teardown ,it will close the browser and deletete the cookies after testcase has executed
#     print(' It will execute at last')

def test_fixturedemo(setup):   #when pass setup as parameter then it will connect to fixture
    print('it will execute steps in fixturedemo method')