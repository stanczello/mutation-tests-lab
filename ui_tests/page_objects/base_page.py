from abc import ABC

class BasePage(ABC):
    def __init__(self, driver, config):
        self.driver = driver
        self.base_url = config['baseUrl']
        self.page = "/"
        self.page_url = self.base_url + self.page

    def open(self):
        self.driver.get(self.page_url)