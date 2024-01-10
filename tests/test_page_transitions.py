from selenium.webdriver.support import expected_conditions
from locators import *
from selenium.webdriver.support.wait import WebDriverWait


class TestPageTransitions:
    def test_transition_from_main_page_to_my_account_page(self, authorized_driver):
        authorized_driver.find_element(*Locators.MY_ACCOUNT_LINK).click()
        WebDriverWait(authorized_driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.LOGOUT_BUTTON))
        assert authorized_driver.find_element(*Locators.LOGOUT_BUTTON).is_displayed()

    def test_transition_from_my_account_page_to_constructor_via_logo(self, authorized_driver):
        authorized_driver.find_element(*Locators.MY_ACCOUNT_LINK).click()
        WebDriverWait(authorized_driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.LOGOUT_BUTTON))
        authorized_driver.find_element(*Locators.LOGO_LINK).click()
        WebDriverWait(authorized_driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert authorized_driver.find_element(*Locators.BUNS_TAB).is_displayed()

    def test_transition_from_my_account_page_to_constructor_via_constructor(self, authorized_driver):
        authorized_driver.find_element(*Locators.MY_ACCOUNT_LINK).click()
        WebDriverWait(authorized_driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.LOGOUT_BUTTON))
        authorized_driver.find_element(*Locators.CONSTRUCTOR).click()
        WebDriverWait(authorized_driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert authorized_driver.find_element(*Locators.SAUCES_TAB).is_displayed()
