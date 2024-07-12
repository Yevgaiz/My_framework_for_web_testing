def test_valid_login(login_page, valid_user):
    """Test login with valid credentials."""
    dashboard_page = login_page.perform_successful_login(valid_user)
    assert dashboard_page.is_displayed(), "Dashboard page is not displayed"


def test_redirecting_to_orangehrm(login_page):
    """Test redirecting to the OrangeHRM website in a new tab."""
    expected_url = "https://www.orangehrm.com/"
    login_page.orangehrm_link.click()
    assert login_page.switch_to_second_tab_and_check_url() == expected_url, "Redirection was not performed"


def test_logo_is_displayed(login_page):
    """Test verifying the presence and display of the logo on the login page."""
    assert login_page.is_logo_displayed(), "Logo is not displayed on the login page."

