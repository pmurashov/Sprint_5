from selenium.webdriver.support import expected_conditions
from Sprint_5.locators import Locators
from selenium.webdriver.support.wait import WebDriverWait

class TestLogin:
    def test_login_via_button_on_main_page(self, driver, credentials):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locators.LOGIN_MAIN_PAGE_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.EMAIL_INPUT).clear()
        driver.find_element(*Locators.PASSWORD_INPUT).clear()

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(credentials['login'])
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(credentials['password'])
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert len(driver.find_elements(*Locators.ORDER_BUTTON)) == 1

    def test_login_via_my_account_button(self, driver, credentials):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locators.MY_ACCOUNT_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.EMAIL_INPUT).clear()
        driver.find_element(*Locators.PASSWORD_INPUT).clear()

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(credentials['login'])
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(credentials['password'])
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert len(driver.find_elements(*Locators.ORDER_BUTTON)) == 1

    def test_login_via_registration_form(self, driver, credentials):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*Locators.LOGIN_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.EMAIL_INPUT).clear()
        driver.find_element(*Locators.PASSWORD_INPUT).clear()

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(credentials['login'])
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(credentials['password'])
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert len(driver.find_elements(*Locators.ORDER_BUTTON)) == 1

    def test_login_via_forgot_password_link(self, driver, credentials):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(*Locators.FORGOT_PASSWORD_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_LINK))
        driver.find_element(*Locators.LOGIN_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.EMAIL_INPUT).clear()
        driver.find_element(*Locators.PASSWORD_INPUT).clear()

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(credentials['login'])
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(credentials['password'])
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert len(driver.find_elements(*Locators.ORDER_BUTTON)) == 1
