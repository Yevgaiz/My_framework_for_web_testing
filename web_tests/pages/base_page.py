from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator, timeout=3, condition=EC.visibility_of_element_located):
        return WebDriverWait(self.driver, timeout).until(condition(locator))

    def wait_for_condition(self, condition, timeout=5):
        return WebDriverWait(self.driver, timeout).until(condition)
