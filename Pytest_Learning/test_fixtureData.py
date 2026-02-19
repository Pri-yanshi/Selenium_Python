import pytest

@pytest.mark.usefixtures("dataload")
class TestExample1:
    def test_editProfiles(self,dataload):  #we pass dataload as parameter because we want to print fixture data
        print(dataload)