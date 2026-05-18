import time
import pytest
from SauceDemo_Framework.Pages.elements import HomePag

@pytest.mark.parametrize(
    "uname, uemail, cadd, padd",
    [
        ("Priyanshi", "priya@gmail.com", "Delhi", "Mumbai")
        # ("Rahul", "rahul@gmail.com", "Noida", "Lucknow"),
        # ("Aman", "aman@gmail.com", "Pune", "Jaipur")
    ]
)
def test_home(browser_details,uname, uemail, cadd, padd):
    driver=browser_details
    hom=HomePag(driver)
    hom.open_url()
    hom.open_element()
    hom.text_box(uname, uemail, cadd, padd)
    hom.check_box()
    time.sleep(15)

