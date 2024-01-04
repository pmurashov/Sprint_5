from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Sprint_5.locators import *


class TestTabTransitions:
    def test_transition_to_sauces_tab(self, authorized_driver):
        WebDriverWait(authorized_driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
        authorized_driver.find_element(*Locators.SAUCES_TAB).click()
        assert "current" in authorized_driver.find_element(*Locators.SAUCES_TAB).get_attribute("class")

    def test_transition_to_fillings_tab(self, authorized_driver):
        WebDriverWait(authorized_driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
        authorized_driver.find_element(*Locators.FILLINGS_TAB).click()
        assert "current" in authorized_driver.find_element(*Locators.FILLINGS_TAB).get_attribute("class")

    def test_transition_to_buns_tab(self, authorized_driver):
        WebDriverWait(authorized_driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
        authorized_driver.find_element(*Locators.SAUCES_TAB).click()
        authorized_driver.find_element(*Locators.BUNS_TAB).click()
        assert "current" in authorized_driver.find_element(*Locators.BUNS_TAB).get_attribute("class")
