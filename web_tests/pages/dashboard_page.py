from selenium.webdriver.common.by import By
from web_tests.pages.base_page import BasePage


class DashboardPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    TIME_AT_WORK_CONTAINER = (
        By.XPATH, "//div[@class='oxd-sheet oxd-sheet--rounded oxd-sheet--white orangehrm-dashboard-widget']")

    @property
    def time_at_work_container(self):
        return self.get_element(DashboardPage.TIME_AT_WORK_CONTAINER)

    def is_displayed(self):
        return self.time_at_work_container.is_displayed()
