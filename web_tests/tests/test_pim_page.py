def test_load_pim_page(pim_page):
    """Test to verify that the PIM page loads successfully and required elements are displayed."""
    assert pim_page.pim_button.is_displayed(), "PIM button is not displayed"
    assert pim_page.header.is_displayed(), "PIM header is not displayed"


def test_add_employee(pim_page, employee, add_employee):
    """Test to add a new employee and verify the addition success pop-up."""
    assert add_employee, "Employee was not added"


def test_delete_employee(pim_page, employee, add_employee):
    """Test to delete an existing employee and verify the deletion success pop-up."""
    assert add_employee, "Employee was not added"
    pim_page.click_pim_button()
    pim_page.delete_employee(employee)
    assert pim_page.success_deletion_pop_up_displayed(), "Employee was not deleted"
