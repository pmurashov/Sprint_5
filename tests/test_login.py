from selenium.webdriver.support import expected_conditions
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:
    def test_login_via_button_on_main_page(self, unauthorized_driver, credentials):
        unauthorized_driver.find_element(*Locators.LOGIN_MAIN_PAGE_BUTTON).click()
        WebDriverWait(unauthorized_driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        unauthorized_driver.find_element(*Locators.EMAIL_INPUT).clear()
        unauthorized_driver.find_element(*Locators.PASSWORD_INPUT).clear()

        unauthorized_driver.find_element(*Locators.EMAIL_INPUT).send_keys(credentials['login'])
        unauthorized_driver.find_element(*Locators.PASSWORD_INPUT).send_keys(credentials['password'])
        unauthorized_driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(unauthorized_driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert unauthorized_driver.find_element(*Locators.ORDER_BUTTON).is_displayed()

    def test_login_via_my_account_button(self, unauthorized_driver, credentials):
        unauthorized_driver.find_element(*Locators.MY_ACCOUNT_LINK).click()
        WebDriverWait(unauthorized_driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        unauthorized_driver.find_element(*Locators.EMAIL_INPUT).clear()
        unauthorized_driver.find_element(*Locators.PASSWORD_INPUT).clear()

        unauthorized_driver.find_element(*Locators.EMAIL_INPUT).send_keys(credentials['login'])
        unauthorized_driver.find_element(*Locators.PASSWORD_INPUT).send_keys(credentials['password'])
        unauthorized_driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(unauthorized_driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert unauthorized_driver.find_element(*Locators.ORDER_BUTTON).is_displayed()

    def test_login_via_registration_form(self, unauthorized_driver, credentials):
        unauthorized_driver.get("https://stellarburgers.nomoreparties.site/register")
        unauthorized_driver.find_element(*Locators.LOGIN_LINK).click()
        WebDriverWait(unauthorized_driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        unauthorized_driver.find_element(*Locators.EMAIL_INPUT).clear()
        unauthorized_driver.find_element(*Locators.PASSWORD_INPUT).clear()

        unauthorized_driver.find_element(*Locators.EMAIL_INPUT).send_keys(credentials['login'])
        unauthorized_driver.find_element(*Locators.PASSWORD_INPUT).send_keys(credentials['password'])
        unauthorized_driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(unauthorized_driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert unauthorized_driver.find_element(*Locators.ORDER_BUTTON).is_displayed()

    def test_login_via_forgot_password_link(self, unauthorized_driver, credentials):
        unauthorized_driver.get("https://stellarburgers.nomoreparties.site/login")
        unauthorized_driver.find_element(*Locators.FORGOT_PASSWORD_LINK).click()
        WebDriverWait(unauthorized_driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.LOGIN_LINK))
        unauthorized_driver.find_element(*Locators.LOGIN_LINK).click()
        WebDriverWait(unauthorized_driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        unauthorized_driver.find_element(*Locators.EMAIL_INPUT).clear()
        unauthorized_driver.find_element(*Locators.PASSWORD_INPUT).clear()

        unauthorized_driver.find_element(*Locators.EMAIL_INPUT).send_keys(credentials['login'])
        unauthorized_driver.find_element(*Locators.PASSWORD_INPUT).send_keys(credentials['password'])
        unauthorized_driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(unauthorized_driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert unauthorized_driver.find_element(*Locators.ORDER_BUTTON).is_displayed()
