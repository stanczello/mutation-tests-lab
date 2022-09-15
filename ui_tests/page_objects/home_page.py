from selenium.webdriver.common.by import By

from ui_tests.page_objects.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver, config):
        super().__init__(driver, config)

    def get_title(self):
        return self.driver.find_element(By.CLASS_NAME, "heading")

    def get_subheader(self):
        return self.driver.find_element(By.CSS_SELECTOR, "h2")