#Any pytest file should start with 'test_' or end with '_test'
#Pytest method names should start with test
#Any code should be wrapped in method only
#Method name should have sense
#-k stands for method name execution, -s logs in output, -v stands for more info metadata
# you can run any specific file with 'py.test <filename>'
# you can mark(tag) tests @pytst.mark.smoke and then run with -m
#fixture are used as setup and teardown for test case
#conftest file to generalize fixture and make it available to all test cases.
# datadriven and parameterization can be done with return statement in tuple format
# when you define fixture scope to class only,it will run once before class initialization and at the end
import pytest


def test_firstProgram(setup):
    print("Hello World")
@pytest.mark.xfail    # its running but not reporting
def test_secTestCase():
    age=17
    assert age<18, 'Your age should be less than 18'

def test_crossbrowser(cross_browser):
    print(cross_browser[1])

