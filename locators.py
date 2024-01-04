from selenium.webdriver.common.by import By


class Locators:
    # форма авторизации
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/parent::div/input")  # поле ввода email
    PASSWORD_INPUT = (By.XPATH, ".//input[@name='Пароль']")  # поле ввода пароля
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")  # кнопка Войти
    REGISTRATION_LINK = (By.XPATH, ".//a[text()='Зарегистрироваться']")  # ссылка Зарегистрироваться
    FORGOT_PASSWORD_LINK = (By.XPATH, ".//a[text()='Восстановить пароль']")  # ссылка Восстановить пароль

    # форма регистрации
    NAME_INPUT = (By.XPATH, ".//label[text()='Имя']/parent::div/input")  # поле ввода email
    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")  # кнопка Зарегистрироваться
    LOGIN_LINK = (By.XPATH, ".//a[text()='Войти']")  # ссылка "Войти"
    INCORRECT_PASSWORD_TEXT = (By.XPATH, ".//p[text()='Некорректный пароль']")  # алерт "Некорректный пароль"

    # главная страница
    MY_ACCOUNT_LINK = (By.XPATH, ".//p[text()='Личный Кабинет']/parent::a")  # личный кабинет
    LOGIN_MAIN_PAGE_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # кнопка войти в аккаунт
    ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")  # кнопка Оформить заказ
    CONSTRUCTOR = (By.XPATH, ".//p[text()='Конструктор']/parent::a")  # конструктор
    BUNS_TAB = (By.XPATH, ".//span[text()='Булки']/parent::div")  # вкладка булки
    SAUCES_TAB = (By.XPATH, ".//span[text()='Соусы']/parent::div")  # вкладка соусы
    FILLINGS_TAB = (By.XPATH, ".//span[text()='Начинки']/parent::div")  # вкладка начинки
    LOGO_LINK = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")  # логотип Stellar Burgers

    # личный кабинет
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")  # кнопка выйти
    ACCOUNT_NAME = (By.XPATH, ".//label[text()='Имя']/parent::div/input")  # поле Имя
    ACCOUNT_LOGIN = (By.XPATH, ".//label[text()='Логин']/parent::div/input")  # поле Логин
