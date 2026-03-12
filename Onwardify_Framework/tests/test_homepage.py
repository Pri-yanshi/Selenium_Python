
from Onwardify_Framework.pages.home_page import HomePage

def test_website(Browser_info):
    driver =Browser_info
    home = HomePage(driver)
    home.open_website()
    assert "Onward" in home.get_title()
    logs= home.console_log()
    error=[log for log in logs if log['level'] == 'SEVERE']
    print(error)
    assert len(error)==0

    title = home.get_title()
    assert "Onward" in title or "Ticket" in title

    url = home.get_url()
    assert url.startswith("https://")


