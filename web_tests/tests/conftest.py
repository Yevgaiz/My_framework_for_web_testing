import pytest
from selenium import webdriver

from web_tests.helpers.employee import Employee
from web_tests.helpers.user import User
from web_tests.pages.login_page import LoginPage
from web_tests.pages.pim_page import PimPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
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
