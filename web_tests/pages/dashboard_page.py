from selenium.webdriver.common.by import By
from web_tests.pages.base_page import BasePage


class DashboardPage(BasePage):
    # URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard'

    def __init__(self, driver):
        super().__init__(driver)

    DASHBOARD_TITLE = (By.XPATH, '//h6[text()="Dashboard"]')

    # def load(self):
    #     self.driver.get(self.URL)

    @property
    def dashboard_title(self):
        return self.get_element(DashboardPage.DASHBOARD_TITLE)

    def is_displayed(self):
        return self.dashboard_title.is_displayed()

