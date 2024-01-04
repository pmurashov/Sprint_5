import pytest
import random
import exrex
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Sprint_5.locators import *


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def new_login():
    domain = ["ya.ru", "yandex.ru", "gmail.com"]
    return f"pavel_murashov_6_{random.randint(100, 999)}@{random.choice(domain)}"


@pytest.fixture()
def new_password():
    return exrex.getone("[A-Z][a-z][0-9]{6}")


@pytest.fixture()
def credentials():
    creds_dict = {"login": "pmurashov_6@gmail.com", "password": "qwerty"}
    return creds_dict


@pytest.fixture()
def authorized_driver(driver, credentials):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
    driver.find_element(*Locators.EMAIL_INPUT).clear()
    driver.find_element(*Locators.PASSWORD_INPUT).clear()
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(credentials['login'])
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(credentials['password'])
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.MY_ACCOUNT_LINK))
    yield driver
