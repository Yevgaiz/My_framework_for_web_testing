from selenium.webdriver.common.by import By
from web_tests.pages.base_page import BasePage


class AddEmployeePage(BasePage):
    FIRST_NAME_INPUT = (By.NAME, 'firstName')
    LAST_NAME_INPUT = (By.NAME, 'lastName')
    SAVE_BUTTON = (By.XPATH, '//button[@type="submit"]')

    @property
    def first_name_input(self):
        return self.get_element(AddEmployeePage.FIRST_NAME_INPUT)

    @property
    def last_name_input(self):
        return self.get_element(AddEmployeePage.LAST_NAME_INPUT)

    @property
    def save_button(self):
        return self.get_element(AddEmployeePage.SAVE_BUTTON)

    def enter_first_name(self, first_name):
        self.first_name_input.send_keys(first_name)
        return self

    def enter_last_name(self, last_name):
        self.last_name_input.send_keys(last_name)
        return self

    def click_save_button(self):
        self.save_button.click()

    def add_employee(self, employee):
        self.enter_first_name(employee.first_name)
        self.enter_last_name(employee.last_name)
        self.click_save_button()
        return self
