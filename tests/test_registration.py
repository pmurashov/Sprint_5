import random

import pytest
from selenium.webdriver.support import expected_conditions

from Sprint_5.locators import *
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration:
    def test_register_user(self, driver, new_login, new_password):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(*Locators.REGISTRATION_LINK).click()
        driver.find_element(*Locators.NAME_INPUT).send_keys(new_login[:new_login.find("@")])
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(new_login)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(new_password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(new_login)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(new_password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.MY_ACCOUNT_LINK))

        driver.find_element(*Locators.MY_ACCOUNT_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGOUT_BUTTON))

        login_attribute = driver.find_element(*Locators.ACCOUNT_LOGIN).get_attribute("value")
        assert new_login in login_attribute, f"Значение атрибута {login_attribute}"

    def test_cannot_register_with_empty_name_field(self, driver, new_login, new_password):
        url = "https://stellarburgers.nomoreparties.site/register"
        driver.get(url)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(new_login)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(new_password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        assert driver.current_url == url

    @pytest.mark.parametrize("login", [f"pavel_murashov_{random.randint(100000, 999999)}",
                                       f"pavel_murashov{random.randint(100000, 999999)}@mailru",
                                       f"pmurashovmail{random.randint(100000, 999999)}.ru",
                                       f"pmurashov{random.randint(100000, 999999)}.mail@ru"])
    def test_cannot_register_with_email_incorrect_mask(self, driver, login, new_password):
        url = "https://stellarburgers.nomoreparties.site/register"
        driver.get(url)
        driver.find_element(*Locators.NAME_INPUT).send_keys(login)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(login)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(new_password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        assert driver.current_url == url

    def test_cannot_register_with_password_length_less_than_6_chars(self, driver, new_login, new_password):
        url = "https://stellarburgers.nomoreparties.site/register"
        driver.get(url)
        driver.find_element(*Locators.NAME_INPUT).send_keys(new_login[:new_login.find("@")])
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(new_login)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(new_password[:5])
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        assert driver.current_url == url
        assert len(driver.find_elements(*Locators.INCORRECT_PASSWORD_TEXT)) == 1
