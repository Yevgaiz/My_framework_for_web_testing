import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from web_tests.helpers.employee import Employee
from web_tests.helpers.user import User
from web_tests.pages.login_page import LoginPage
from web_tests.pages.pim_page import PimPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def valid_user():
    return User('Admin', 'admin123')


@pytest.fixture()
def employee():
    return Employee('Ivan', 'Ivanov')


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver).load()


@pytest.fixture()
def pim_page(driver, valid_user):
    pim_page = PimPage(driver)
    pim_page.load_pim_page(valid_user)
    return pim_page


@pytest.fixture()
def add_employee(pim_page, employee):
    add_employee_page = pim_page.click_add_button()
    add_employee_page.add_employee(employee)
    return pim_page.success_addition_pop_up_displayed()
