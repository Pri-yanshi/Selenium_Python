import pytest

@pytest.mark.usefixtures('setup')  #this fixture will automatically pass to all methods of class
class TestExample:

   def test_fixturedemo1(self):
      print('it will execute steps in fixturedemo1 method1')

   def test_fixturedemo2(self):
      print('it will execute steps in fixturedemo2 method2')

   def test_fixturedemo3(self):
      print('it will execute steps in fixturedemo3 method3')

   def test_fixturedemo4(self):
      print('it will execute steps in fixturedemo4 method4')