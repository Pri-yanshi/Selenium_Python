class HomePage:
    def __init__(self,driver):
        self.driver = driver

    def open_website(self):
        self.driver.get("https://onwardify.com/")

    def get_title(self):
        return self.driver.title
    def get_url(self):
        return self.driver.current_url
    def console_log(self):
        return self.driver.get_log("browser")