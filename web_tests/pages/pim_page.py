from selenium.webdriver.common.by import By
from web_tests.pages.add_employee_page import AddEmployeePage
from web_tests.pages.base_page import BasePage
from web_tests.pages.login_page import LoginPage
from selenium.webdriver.support import expected_conditions as EC


class PimPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    PIM_BUTTON = (By.XPATH, '//a[@href="/web/index.php/pim/viewPimModule"]')
    ADD_BUTTON = (By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]')
    HEADER = (By.XPATH, '//h6[text()="PIM"]')
    SUCCESS_ADDITION_POP_UP = (By.ID, 'oxd-toaster_1')
    SUCCESS_DELETION_POP_UP = (By.XPATH, "//div[@class='oxd-toast-content oxd-toast-content--success']")
    EMPLOYEE_NAME_INPUT = (By.XPATH, "//input[@placeholder='Type for hints...']")
    SEARCH_BUTTON = (By.XPATH, '//button[text()=" Search "]')
    DELETE_BUTTON = (By.XPATH, '//i[@class="oxd-icon bi-trash"]')
    CONFIRM_DELETE_BUTTON = (By.XPATH, '//button[text()=" Yes, Delete "]')

    @property
    def pim_button(self):
        return self.get_element(PimPage.PIM_BUTTON)

    @property
    def add_button(self):
        return self.get_element(PimPage.ADD_BUTTON)

    @property
    def header(self):
        return self.get_element(PimPage.HEADER)

    @property
    def success_addition_pop_up(self):
        return self.get_element(PimPage.SUCCESS_ADDITION_POP_UP)

    @property
    def success_deletion_pop_up(self):
        return self.get_element(PimPage.SUCCESS_DELETION_POP_UP)
    @property
    def employee_name_input(self):
        return self.get_element(PimPage.EMPLOYEE_NAME_INPUT)

    @property
    def search_button(self):
        return self.get_element(PimPage.SEARCH_BUTTON)

    @property
    def delete_button(self):
        return self.get_element(PimPage.DELETE_BUTTON)

    @property
    def confirm_delete_button(self):
        return self.get_element(PimPage.CONFIRM_DELETE_BUTTON)

    def load_pim_page(self, user):
        login_page = LoginPage(self.driver)
        login_page.load().perform_successful_login(user)
        self.pim_button.click()
        return self

    def click_add_button(self):
        self.add_button.click()
        return AddEmployeePage(self.driver)

    def click_search_button(self):
        self.search_button.click()
        return self

    def success_addition_pop_up_displayed(self):
        return self.wait_for_condition(EC.visibility_of_element_located(PimPage.SUCCESS_ADDITION_POP_UP))

    def success_deletion_pop_up_displayed(self):
        return self.wait_for_condition(EC.visibility_of_element_located(PimPage.SUCCESS_DELETION_POP_UP))

    def fill_employee_name_input(self, employee):
        return self.employee_name_input.send_keys(employee)

    def search_employee(self, employee):
        self.fill_employee_name_input(employee.first_name + " " + employee.last_name)
        self.click_search_button()
        return self

    def delete_employee(self, employee):
        self.search_employee(employee)
        self.delete_button.click()
        self.confirm_delete_button.click()
        return self
