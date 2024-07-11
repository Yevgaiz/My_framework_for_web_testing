from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from web_tests.pages.base_page import BasePage
from web_tests.pages.dashboard_page import DashboardPage


class LoginPage(BasePage):
    URL = 'https://opensource-demo.orangehrmlive.com/'

    def __init__(self, driver):
        super().__init__(driver)

    USERNAME_INPUT_FIELD = (By.NAME, 'username')
    PASSWORD_INPUT_FIELD = (By.NAME, 'password')
    LOGIN_BUTTON = (By.XPATH, '//button[@type="submit"]')
    ORANGEHRM_lINK = (By.XPATH, '//a[@href="http://www.orangehrm.com"]')
    ORANGEHRM_LOGO = (By.XPATH, '//img[@alt="company-branding"]')

    @property
    def username_input_field(self):
        return self.get_element(LoginPage.USERNAME_INPUT_FIELD)

    @property
    def password_input_field(self):
        return self.get_element(LoginPage.PASSWORD_INPUT_FIELD)

    @property
    def login_button(self):
        return self.get_element(LoginPage.LOGIN_BUTTON)

    @property
    def orangehrm_link(self):
        return self.get_element(LoginPage.ORANGEHRM_lINK)

    def load(self):
        self.driver.get(self.URL)
        return self

    def enter_username(self, user):
        self.username_input_field.send_keys(user.username)
        return self

    def enter_password(self, user):
        self.password_input_field.send_keys(user.password)
        return self

    def click_login_button(self):
        self.login_button.click()

    def login(self, user):
        self.enter_username(user)
        self.enter_password(user)
        self.click_login_button()

    def perform_successful_login(self, user):
        self.login(user)
        return DashboardPage(self.driver)

    def switch_to_second_tab_and_check_url(self, expected_url):
        self.wait_for_condition(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])
        return self.wait_for_condition(EC.url_contains(expected_url))

    def is_logo_displayed(self):
        logo = self.get_element(LoginPage.ORANGEHRM_LOGO)
        return logo.is_displayed()
