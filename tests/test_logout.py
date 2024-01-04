from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Sprint_5.locators import *


class TestLogout:
    def test_logout(self, authorized_driver):
        authorized_driver.find_element(*Locators.MY_ACCOUNT_LINK).click()
        WebDriverWait(authorized_driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.LOGOUT_BUTTON))
        authorized_driver.find_element(*Locators.LOGOUT_BUTTON).click()
        WebDriverWait(authorized_driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        assert "/login" in authorized_driver.current_url
