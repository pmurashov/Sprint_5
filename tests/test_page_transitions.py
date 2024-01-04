from selenium.webdriver.support import expected_conditions
from Sprint_5.locators import *
from selenium.webdriver.support.wait import WebDriverWait


class TestPageTransitions:
    def test_transition_from_main_page_to_my_account_page(self, authorized_driver):
        authorized_driver.find_element(*Locators.MY_ACCOUNT_LINK).click()
        WebDriverWait(authorized_driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.LOGOUT_BUTTON))
        assert len(authorized_driver.find_elements(*Locators.LOGOUT_BUTTON)) == 1

    def test_transition_from_my_account_page_to_constructor_via_logo(self, authorized_driver):
        authorized_driver.find_element(*Locators.MY_ACCOUNT_LINK).click()
        WebDriverWait(authorized_driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.LOGOUT_BUTTON))
        authorized_driver.find_element(*Locators.LOGO_LINK).click()
        WebDriverWait(authorized_driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert len(authorized_driver.find_elements(*Locators.BUNS_TAB)) == 1

    def test_transition_from_my_account_page_to_constructor_via_constructor(self, authorized_driver):
        authorized_driver.find_element(*Locators.MY_ACCOUNT_LINK).click()
        WebDriverWait(authorized_driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.LOGOUT_BUTTON))
        authorized_driver.find_element(*Locators.CONSTRUCTOR).click()
        WebDriverWait(authorized_driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert len(authorized_driver.find_elements(*Locators.SAUCES_TAB)) == 1
